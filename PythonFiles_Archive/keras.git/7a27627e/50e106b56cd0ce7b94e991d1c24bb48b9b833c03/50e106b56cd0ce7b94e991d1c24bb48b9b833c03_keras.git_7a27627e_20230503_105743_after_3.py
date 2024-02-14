from keras_core import operations as ops
from keras_core.api_export import keras_core_export
from keras_core.layers.merging.base_merge import Merge


@keras_core_export("keras_core.layers.Maximum")
class Maximum(Merge):
    """Computes element-wise maximum on a list of inputs.

    It takes as input a list of tensors, all of the same shape,
    and returns a single tensor (also of the same shape).

    Examples:

    >>> input_shape = (2, 3, 4)
    >>> x1 = np.random.rand(*input_shape)
    >>> x2 = np.random.rand(*input_shape)
    >>> y = keras_core.layers.Maximum()([x1, x2])

    Usage in a Keras model:

    >>> input1 = keras_core.layers.Input(shape=(16,))
    >>> x1 = keras_core.layers.Dense(8, activation='relu')(input1)
    >>> input2 = keras_core.layers.Input(shape=(32,))
    >>> x2 = keras_core.layers.Dense(8, activation='relu')(input2)
    >>> # equivalent to `y = keras_core.layers.maximum([x1, x2])`
    >>> y = keras_core.layers.Maximum()([x1, x2])
    >>> out = keras_core.layers.Dense(4)(y)
    >>> model = keras_core.models.Model(inputs=[input1, input2], outputs=out)

    """

    def _merge_function(self, inputs):
        output = inputs[0]
        for i in range(1, len(inputs)):
            output = ops.maximum(output, inputs[i])
        return output


@keras_core_export("keras_core.layers.maximum")
def maximum(inputs, **kwargs):
    """Functional interface to the `keras_core.layers.Maximum` layer.

    Args:
        inputs: A list of input tensors , all of the same shape.
        **kwargs: Standard layer keyword arguments.

    Returns:
        A tensor as the element-wise product of the inputs with the same
        shape as the inputs.

    Examples:

    >>> input_shape = (2, 3, 4)
    >>> x1 = np.random.rand(*input_shape)
    >>> x2 = np.random.rand(*input_shape)
    >>> y = keras_core.layers.maximum([x1, x2])

    Usage in a Keras model:

    >>> input1 = keras_core.layers.Input(shape=(16,))
    >>> x1 = keras_core.layers.Dense(8, activation='relu')(input1)
    >>> input2 = keras_core.layers.Input(shape=(32,))
    >>> x2 = keras_core.layers.Dense(8, activation='relu')(input2)
    >>> y = keras_core.layers.maximum([x1, x2])
    >>> out = keras_core.layers.Dense(4)(y)
    >>> model = keras_core.models.Model(inputs=[input1, input2], outputs=out)

    """
    return Maximum(**kwargs)(inputs)
