# Copyright 2023 The Keras Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import tensorflow.compat.v2 as tf

from keras.initializers import TruncatedNormal
from keras.layers.rnn import Wrapper

# isort: off
from tensorflow.python.util.tf_export import keras_export


# Adapted from TF-Addons implementation
@keras_export("keras.layers.SpectralNormalization", v1=[])
class SpectralNormalization(Wrapper):
    """Performs spectral normalization on weights.

    This wrapper controls the Lipschitz constant of the layer by
    constraining its spectral norm, which can stabilize the training of GANs.
    See [Spectral Normalization for GAN](https://arxiv.org/abs/1802.05957).

    Args:
      layer: a `tf.keras.layers.Layer` instance that
        has either a `kernel` or an `embeddings` attribute.
      power_iterations: `int`, the number of iterations during normalization.

    Examples:
      Wrap `tf.keras.layers.Conv2D`:
      >>> x = np.random.rand(1, 10, 10, 1)
      >>> conv2d = SpectralNormalization(tf.keras.layers.Conv2D(2, 2))
      >>> y = conv2d(x)
      >>> y.shape
      TensorShape([1, 9, 9, 2])

      Wrap `tf.keras.layers.Dense`:
      >>> x = np.random.rand(1, 10, 10, 1)
      >>> dense = SpectralNormalization(tf.keras.layers.Dense(10))
      >>> y = dense(x)
      >>> y.shape
      TensorShape([1, 10, 10, 10])
    """

    def __init__(self, layer, power_iterations=1, **kwargs):
        super().__init__(layer, **kwargs)
        if power_iterations <= 0:
            raise ValueError(
                "`power_iterations` should be greater than zero, got "
                f"`power_iterations={power_iterations}`"
            )
        self.power_iterations = power_iterations

    def build(self, input_shape):
        super().build(input_shape)
        input_shape = tf.TensorShape(input_shape)
        self.input_spec = tf.keras.layers.InputSpec(
            shape=[None] + input_shape[1:]
        )

        if hasattr(self.layer, "kernel"):
            self.kernel = self.layer.kernel
        elif hasattr(self.layer, "embeddings"):
            self.kernel = self.layer.embeddings
        else:
            raise ValueError(
                f"{type(self.layer).__name__} object has no attribute 'kernel' "
                "nor 'embeddings'"
            )

        self.kernel_shape = self.kernel.shape.as_list()

        self.sn_u = self.add_weight(
            shape=(1, self.self.kernel_shape[-1]),
            initializer=TruncatedNormal(stddev=0.02),
            trainable=False,
            name="sn_u",
            dtype=self.kernel.dtype,
        )

    def call(self, inputs, training=False):
        if training:
            self.normalize_weights()

        output = self.layer(inputs)
        return output

    def compute_output_shape(self, input_shape):
        return tf.TensorShape(
            self.layer.compute_output_shape(input_shape).as_list()
        )

    def normalize_weights(self):
        """Generate spectral normalized weights.

        This method will update the value of `self.kernel` with the
        spectral normalized value, so that the layer is ready for `call()`.
        """

        w = tf.reshape(self.kernel, [-1, self.self.kernel_shape[-1]])
        u = self.sn_u

        # check for zeroes weights
        if not tf.reduce_all(tf.equal(w, 0.0)):
            for _ in range(self.power_iterations):
                v = tf.math.l2_normalize(tf.matmul(u, w, transpose_b=True))
                u = tf.math.l2_normalize(tf.matmul(v, w))
            u = tf.stop_gradient(u)
            v = tf.stop_gradient(v)
            sigma = tf.matmul(tf.matmul(v, w), u, transpose_b=True)
            self.sn_u.assign(tf.cast(u, self.sn_u.dtype))
            self.kernel.assign(
                tf.cast(
                    tf.reshape(self.kernel / sigma, self.self.kernel_shape),
                    self.kernel.dtype,
                )
            )

    def get_config(self):
        config = {"power_iterations": self.power_iterations}
        base_config = super().get_config()
        return {**base_config, **config}
