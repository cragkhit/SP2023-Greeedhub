from __future__ import absolute_import
import theano
import theano.tensor as T
import numpy as np
import warnings
import time
from collections import deque

from .utils.generic_utils import Progbar

class CallbackList(object):

    def __init__(self, callbacks, queue_length=10):
        self.callbacks = callbacks
        self.queue_length = queue_length

    def append(self, callback):
        self.callbacks.append(callback)

    def _set_params(self, params):
        for callback in self.callbacks:
            callback._set_params(params)

    def _set_model(self, model):
        for callback in self.callbacks:
            callback._set_model(model)

    def on_epoch_begin(self, epoch):
        for callback in self.callbacks:
            callback.on_epoch_begin(epoch)
        self._delta_t_batch = 0.
        self._delta_ts_batch_begin = deque([], maxlen=self.queue_length)
        self._delta_ts_batch_end = deque([], maxlen=self.queue_length)

    def on_epoch_end(self, epoch, val_loss, val_acc):
        for callback in self.callbacks:
            callback.on_epoch_end(epoch, val_loss, val_acc)

    def on_batch_begin(self, batch):
        t_before_callbacks = time.time()
        for callback in self.callbacks:
            callback.on_batch_begin(batch)
        self._delta_ts_batch_begin.append(time.time() - t_before_callbacks)
        delta_t_median = np.median(self._delta_ts_batch_begin)
        if self._delta_t_batch > 0. and delta_t_median > 0.95 * self._delta_t_batch \
            and delta_t_median > 0.1:
            warnings.warn('Method on_batch_begin() is slow compared '
                'to the batch update (%f). Check your callbacks.' % delta_t_median)
        self._t_enter_batch = time.time()

    def on_batch_end(self, batch, indices, loss, accuracy):
        self._delta_t_batch = time.time() - self._t_enter_batch
        t_before_callbacks = time.time()
        for callback in self.callbacks:
            callback.on_batch_end(batch, indices, loss, accuracy)
        self._delta_ts_batch_end.append(time.time() - t_before_callbacks)
        delta_t_median = np.median(self._delta_ts_batch_end)
        if self._delta_t_batch > 0. and delta_t_median > 0.95 * self._delta_t_batch \
            and delta_t_median > 0.1:
            warnings.warn('Method on_batch_end() is slow compared '
                'to the batch update (%f). Check your callbacks.' % delta_t_median)

    def on_train_begin(self):
        for callback in self.callbacks:
            callback.on_train_begin()

    def on_train_end(self):
        for callback in self.callbacks:
            callback.on_train_end()


class Callback(object):

    def __init__(self):
        pass

    def _set_params(self, params):
        self.params = params

    def _set_model(self, model):
        self.model = model

    def on_epoch_begin(self, epoch):
        pass

    def on_epoch_end(self, epoch, val_loss, val_acc):
        pass

    def on_batch_begin(self, batch):
        pass

    def on_batch_end(self, batch, indices, loss, accuracy):
        pass

    def on_train_begin(self):
        pass

    def on_train_end(self):
        pass

class History(Callback):

    def on_train_begin(self):
        self.epochs = []
        self.losses = []
        if self.params['show_accuracy']:
            self.accuracies = []
        if self.params['do_validation']:
            self.validation_losses = []
            if self.params['show_accuracy']:
                self.validation_accuracies = []

    def on_epoch_begin(self, epoch):
        self.seen = 0
        self.cum_loss = 0.
        self.cum_accuracy = 0.

    def on_batch_end(self, batch, indices, loss, accuracy):
        batch_length = len(indices)
        self.seen += batch_length
        self.cum_loss += loss * batch_length
        if self.params['show_accuracy']:
            self.cum_accuracy += accuracy * batch_length

    def on_epoch_end(self, epoch, val_loss, val_acc):
        self.epochs.append(epoch)
        self.losses.append(self.cum_loss / self.seen)
        if self.params['show_accuracy']:
            self.accuracies.append(self.cum_accuracy / self.seen)
        if self.params['do_validation']:
            self.validation_losses.append(val_loss)
            if self.params['show_accuracy']:
                self.validation_accuracies.append(val_acc)

class Logger(Callback):

    def on_train_begin(self):
        self.verbose = self.params['verbose']

    def on_epoch_begin(self, epoch):
        if self.verbose:
            print 'Epoch %d' % epoch
            self.progbar = Progbar(target=self.params['nb_sample'], \
                verbose=self.verbose)
        self.current = 0

    def on_batch_begin(self, batch):
        self.log_values = []

    def on_batch_end(self, batch, indices, loss, accuracy):
        self.log_values.append(('loss', loss))
        self.current += len(indices)
        if self.params['show_accuracy']:
            self.log_values.append(('acc.', acc))
        if self.verbose:
            self.progbar.update(self.current, self.log_values)

    def on_epoch_end(self, epoch, val_loss, val_acc):
        # TODO: Show validation scores in the logger
        if self.params['do_validation']:
            self.log_values.append(('val. loss', val_loss))
            if self.params['show_accuracy']:
                self.log_values.append(('val. acc.', val_acc))
