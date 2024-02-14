import torch

from keras_core.optimizers.base_optimizer import BaseOptimizer


class TorchOptimizer(BaseOptimizer):
    def __new__(cls, *args, **kwargs):
        # Import locally to avoid circular imports.
        from keras_core import optimizers
        from keras_core.backend.torch.optimizers import torch_sgd

        OPTIMIZERS = {optimizers.SGD: torch_sgd.SGD}
        if cls in OPTIMIZERS:
            return OPTIMIZERS[cls](*args, **kwargs)
        return super().__new__(cls)

    def _apply_weight_decay(self, variables):
        if self.weight_decay is None:
            return

        torch._foreach_mul_(
            [v.value for v in variables if self._use_weight_decay(v)],
            1 - self.weight_decay * self._get_current_learning_rate(),
        )
