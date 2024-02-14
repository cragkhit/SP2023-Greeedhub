import numpy as np
from tensorflow.python.ops.numpy_ops import np_config

from keras_core import testing
from keras_core.backend.keras_tensor import KerasTensor
from keras_core.operations import numpy as knp

np_config.enable_numpy_behavior()


class NumpyTwoInputOpsShapeTest(testing.TestCase):
    def test_add(self):
        x = KerasTensor((2, 3))
        y = KerasTensor((2, 3))
        self.assertEqual(knp.add(x, y).shape, (2, 3))

        x = KerasTensor((None, 3))
        y = KerasTensor((2, None))
        self.assertEqual(knp.add(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.add(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.add(x, y)

    def test_subtract(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.subtract(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.subtract(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.subtract(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.subtract(x, y)

    def test_multiply(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.multiply(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.multiply(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.multiply(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.multiply(x, y)

    def test_matmul(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([3, 2])
        self.assertEqual(knp.matmul(x, y).shape, (2, 2))

        x = KerasTensor([None, 3, 4])
        y = KerasTensor([3, None, 4, 5])
        self.assertEqual(knp.matmul(x, y).shape, (3, None, 3, 5))

        with self.assertRaises(ValueError):
            x = KerasTensor([3, 4])
            y = KerasTensor([2, 3, 4])
            knp.matmul(x, y)

    def test_power(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.power(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.power(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.power(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.power(x, y)

    def test_divide(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.divide(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.divide(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.divide(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.divide(x, y)

    def test_true_divide(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.true_divide(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.true_divide(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.true_divide(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.true_divide(x, y)

    def test_append(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.append(x, y).shape, (12,))

        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.append(x, y, axis=0).shape, (4, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.append(x, y).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.append(x, y, axis=2)

    def test_arctan2(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.arctan2(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.arctan2(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.arctan2(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.arctan2(x, y)

    def test_cross(self):
        x1 = KerasTensor([2, 3, 3])
        x2 = KerasTensor([1, 3, 2])
        y1 = KerasTensor([2, 3, 3])
        y2 = KerasTensor([None, 1, 2])
        y3 = KerasTensor([2, 3, 2])
        self.assertEqual(knp.cross(x1, y1).shape, (2, 3, 3))
        self.assertEqual(knp.cross(x1, y2).shape, (2, 3, 3))
        self.assertEqual(knp.cross(x2, y2).shape, (None, 3))
        self.assertEqual(knp.cross(x2, y3).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.cross(x, y)

        with self.assertRaises(ValueError):
            x = KerasTensor([4, 3, 3])
            y = KerasTensor([2, 3, 3])
            knp.cross(x, y)

    def test_full_like(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.full_like(x, 2).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.full_like(x, KerasTensor([1, 3])).shape, (None, 3))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.full_like(x, 2).shape, (None, 3, 3))

    def test_greater(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.greater(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.greater(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.greater(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.greater(x, y)

    def test_greater_equal(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.greater_equal(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.greater_equal(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.greater_equal(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.greater_equal(x, y)

    def test_isclose(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.isclose(x, y).shape, (2, 3))

        x = KerasTensor([None, 3])
        y = KerasTensor([2, None])
        self.assertEqual(knp.isclose(x, y).shape, (2, 3))

        x = KerasTensor([2, 3])
        self.assertEqual(knp.isclose(x, 2).shape, (2, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3])
            y = KerasTensor([2, 3, 4])
            knp.isclose(x, y)


class NumpyOneInputOpsShapeTest(testing.TestCase):
    def test_mean(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.mean(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.mean(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.mean(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.mean(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_all(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.all(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.all(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.all(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.all(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_var(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.var(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.var(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.var(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.var(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_sum(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.sum(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.sum(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.sum(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.sum(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_amax(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.amax(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.amax(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.amax(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.amax(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_amin(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.amin(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.amin(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.amin(x, axis=1).shape, (None, 3))
        self.assertEqual(knp.amin(x, axis=1, keepdims=True).shape, (None, 1, 3))

    def test_square(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.square(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.square(x).shape, (None, 3))

    def test_negative(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.negative(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.negative(x).shape, (None, 3))

    def test_abs(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.abs(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.abs(x).shape, (None, 3))

    def test_absolute(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.absolute(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.absolute(x).shape, (None, 3))

    def test_squeeze(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.squeeze(x).shape, (2, 3))

        x = KerasTensor([None, 1])
        self.assertEqual(knp.squeeze(x).shape, (None,))
        self.assertEqual(knp.squeeze(x, axis=1).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor([None, 1])
            knp.squeeze(x, axis=0)

    def test_transpose(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.transpose(x).shape, (3, 2))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.transpose(x).shape, (3, None))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.transpose(x, (2, 0, 1)).shape, (3, None, 3))

    def test_arccos(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.arccos(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.arccos(x).shape, (None, 3))

    def test_arcsin(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.arcsin(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.arcsin(x).shape, (None, 3))

    def test_arctan(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.arctan(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.arctan(x).shape, (None, 3))

    def test_argmax(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.argmax(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.argmax(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.argmax(x, axis=1).shape, (None, 3))

    def test_argmin(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.argmin(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.argmin(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.argmin(x, axis=1).shape, (None, 3))

    def test_argsort(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.argsort(x).shape, (2, 3))
        self.assertEqual(knp.argsort(x, axis=None).shape, (6,))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.argsort(x).shape, (None, 3))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.argsort(x, axis=1).shape, (None, 3, 3))

    def test_array(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.array(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.array(x).shape, (None, 3))

    def test_average(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.average(x).shape, ())

        x = KerasTensor([None, 3])
        weights = KerasTensor([None, 3])
        self.assertEqual(knp.average(x, weights=weights).shape, ())

        x = KerasTensor([None, 3])
        weights = KerasTensor([3])
        self.assertEqual(knp.average(x, axis=1, weights=weights).shape, (None,))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.average(x, axis=1).shape, (None, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([None, 3, 3])
            weights = KerasTensor([None, 4])
            knp.average(x, weights=weights)

    def test_broadcast_to(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.broadcast_to(x, (2, 2, 3)).shape, (2, 2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.broadcast_to(x, (2, 3, 3)).shape, (2, 3, 3))

        with self.assertRaises(ValueError):
            x = KerasTensor([3, 3])
            knp.broadcast_to(x, (2, 2, 3))

    def test_ceil(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.ceil(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.ceil(x).shape, (None, 3))

    def test_clip(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.clip(x, 1, 2).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.clip(x, 1, 2).shape, (None, 3))

    def test_concatenate(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.concatenate([x, y]).shape, (4, 3))
        self.assertEqual(knp.concatenate([x, y], axis=1).shape, (2, 6))

        x = KerasTensor([None, 3])
        y = KerasTensor([None, 3])
        self.assertEqual(
            knp.concatenate(
                [x, y],
            ).shape,
            (None, 3),
        )
        self.assertEqual(knp.concatenate([x, y], axis=1).shape, (None, 6))

        with self.assertRaises(ValueError):
            self.assertEqual(knp.concatenate([x, y], axis=None).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor([None, 3, 5])
            y = KerasTensor([None, 4, 6])
            knp.concatenate([x, y], axis=1)

    def test_conjugate(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.conjugate(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.conjugate(x).shape, (None, 3))

    def test_conj(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.conj(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.conj(x).shape, (None, 3))

    def test_copy(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.copy(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.copy(x).shape, (None, 3))

    def test_cos(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.cos(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.cos(x).shape, (None, 3))

    def test_count_nonzero(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.count_nonzero(x).shape, ())

        x = KerasTensor([None, 3])
        self.assertEqual(knp.count_nonzero(x).shape, ())

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.count_nonzero(x, axis=1).shape, (None, 3))

    def test_cumprod(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.cumprod(x).shape, (6,))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.cumprod(x).shape, (None,))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.cumprod(x, axis=1).shape, (None, 3, 3))

    def test_cumsum(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.cumsum(x).shape, (6,))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.cumsum(x).shape, (None,))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.cumsum(x, axis=1).shape, (None, 3, 3))

    def test_diag(self):
        x = KerasTensor([3])
        self.assertEqual(knp.diag(x).shape, (3, 3))
        self.assertEqual(knp.diag(x, k=3).shape, (6, 6))
        self.assertEqual(knp.diag(x, k=-2).shape, (5, 5))

        x = KerasTensor([3, 5])
        self.assertEqual(knp.diag(x).shape, (3,))
        self.assertEqual(knp.diag(x, k=3).shape, (2,))
        self.assertEqual(knp.diag(x, k=-2).shape, (1,))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.diag(x).shape, (None,))
        self.assertEqual(knp.diag(x, k=3).shape, (None,))

        with self.assertRaises(ValueError):
            x = KerasTensor([2, 3, 4])
            knp.diag(x)

    def test_diagonal(self):
        x = KerasTensor([3, 3])
        self.assertEqual(knp.diagonal(x).shape, (3,))
        self.assertEqual(knp.diagonal(x, offset=1).shape, (2,))

        x = KerasTensor([3, 5, 5])
        self.assertEqual(knp.diagonal(x).shape, (5, 3))

        x = KerasTensor([None, 3, 3])
        self.assertEqual(knp.diagonal(x).shape, (3, None))

        with self.assertRaises(ValueError):
            x = KerasTensor([3])
            knp.diagonal(x)

    def test_exp(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.exp(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.exp(x).shape, (None, 3))

    def test_expand_dims(self):
        x = KerasTensor([2, 3, 4])
        self.assertEqual(knp.expand_dims(x, 0).shape, (1, 2, 3, 4))
        self.assertEqual(knp.expand_dims(x, 1).shape, (2, 1, 3, 4))
        self.assertEqual(knp.expand_dims(x, -2).shape, (2, 3, 1, 4))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.expand_dims(x, 0).shape, (1, None, 3))
        self.assertEqual(knp.expand_dims(x, 1).shape, (None, 1, 3))
        self.assertEqual(knp.expand_dims(x, -2).shape, (None, 1, 3))

    def test_expm1(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.expm1(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.expm1(x).shape, (None, 3))

    def test_flip(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.flip(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.flip(x).shape, (None, 3))

    def test_floor(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.floor(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.floor(x).shape, (None, 3))

    def test_hstack(self):
        x = KerasTensor([2, 3])
        y = KerasTensor([2, 3])
        self.assertEqual(knp.hstack([x, y]).shape, (2, 6))

        x = KerasTensor([None, 3])
        y = KerasTensor([None, 3])
        self.assertEqual(knp.hstack([x, y]).shape, (None, 6))

        x = KerasTensor([None, 3])
        y = KerasTensor([None, None])
        self.assertEqual(knp.hstack([x, y]).shape, (None, None))

    def test_imag(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.imag(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.imag(x).shape, (None, 3))

    def test_isfinite(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.isfinite(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.isfinite(x).shape, (None, 3))

    def test_isinf(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.isinf(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.isinf(x).shape, (None, 3))

    def test_isnan(self):
        x = KerasTensor([2, 3])
        self.assertEqual(knp.isnan(x).shape, (2, 3))

        x = KerasTensor([None, 3])
        self.assertEqual(knp.isnan(x).shape, (None, 3))


class NumpyTwoInputOpsCorretnessTest(testing.TestCase):
    def test_add(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.add(x, y)), np.add(x, y))
        self.assertAllClose(np.array(knp.add(x, z)), np.add(x, z))

        self.assertAllClose(np.array(knp.Add()(x, y)), np.add(x, y))
        self.assertAllClose(np.array(knp.Add()(x, z)), np.add(x, z))

    def test_subtract(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.subtract(x, y)), np.subtract(x, y))
        self.assertAllClose(np.array(knp.subtract(x, z)), np.subtract(x, z))

        self.assertAllClose(np.array(knp.Subtract()(x, y)), np.subtract(x, y))
        self.assertAllClose(np.array(knp.Subtract()(x, z)), np.subtract(x, z))

    def test_multiply(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.multiply(x, y)), np.multiply(x, y))
        self.assertAllClose(np.array(knp.multiply(x, z)), np.multiply(x, z))

        self.assertAllClose(np.array(knp.Multiply()(x, y)), np.multiply(x, y))
        self.assertAllClose(np.array(knp.Multiply()(x, z)), np.multiply(x, z))

    def test_matmul(self):
        x = np.ones([2, 3, 4, 5])
        y = np.ones([2, 3, 5, 6])
        z = np.ones([5, 6])
        self.assertAllClose(np.array(knp.matmul(x, y)), np.matmul(x, y))
        self.assertAllClose(np.array(knp.matmul(x, z)), np.matmul(x, z))

        self.assertAllClose(np.array(knp.Matmul()(x, y)), np.matmul(x, y))
        self.assertAllClose(np.array(knp.Matmul()(x, z)), np.matmul(x, z))

    def test_power(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.power(x, y)), np.power(x, y))
        self.assertAllClose(np.array(knp.power(x, z)), np.power(x, z))

        self.assertAllClose(np.array(knp.Power()(x, y)), np.power(x, y))
        self.assertAllClose(np.array(knp.Power()(x, z)), np.power(x, z))

    def test_divide(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.divide(x, y)), np.divide(x, y))
        self.assertAllClose(np.array(knp.divide(x, z)), np.divide(x, z))

        self.assertAllClose(np.array(knp.Divide()(x, y)), np.divide(x, y))
        self.assertAllClose(np.array(knp.Divide()(x, z)), np.divide(x, z))

    def test_true_divide(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]]])
        self.assertAllClose(
            np.array(knp.true_divide(x, y)), np.true_divide(x, y)
        )
        self.assertAllClose(
            np.array(knp.true_divide(x, z)), np.true_divide(x, z)
        )

        self.assertAllClose(
            np.array(knp.TrueDivide()(x, y)), np.true_divide(x, y)
        )
        self.assertAllClose(
            np.array(knp.TrueDivide()(x, z)), np.true_divide(x, z)
        )

    def test_append(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        z = np.array([[[1, 2, 3], [3, 2, 1]], [[4, 5, 6], [3, 2, 1]]])
        self.assertAllClose(np.array(knp.append(x, y)), np.append(x, y))
        self.assertAllClose(
            np.array(knp.append(x, y, axis=1)), np.append(x, y, axis=1)
        )
        self.assertAllClose(np.array(knp.append(x, z)), np.append(x, z))

        self.assertAllClose(np.array(knp.Append()(x, y)), np.append(x, y))
        self.assertAllClose(
            np.array(knp.Append(axis=1)(x, y)), np.append(x, y, axis=1)
        )
        self.assertAllClose(np.array(knp.Append()(x, z)), np.append(x, z))

    def test_arctan2(self):
        x = np.array([[1.0, 2.0, 3.0], [3.0, 2.0, 1.0]])
        y = np.array([[4.0, 5.0, 6.0], [3.0, 2.0, 1.0]])
        self.assertAllClose(np.array(knp.arctan2(x, y)), np.arctan2(x, y))

        self.assertAllClose(np.array(knp.Arctan2()(x, y)), np.arctan2(x, y))

    def test_cross(self):
        x1 = np.ones([2, 1, 4, 3])
        x2 = np.ones([2, 1, 4, 2])
        y1 = np.ones([2, 1, 4, 3])
        y2 = np.ones([1, 5, 4, 3])
        y3 = np.ones([1, 5, 4, 2])
        self.assertAllClose(np.array(knp.cross(x1, y1)), np.cross(x1, y1))
        self.assertAllClose(np.array(knp.cross(x1, y2)), np.cross(x1, y2))
        self.assertAllClose(np.array(knp.cross(x1, y3)), np.cross(x1, y3))
        self.assertAllClose(np.array(knp.cross(x2, y3)), np.cross(x2, y3))

        self.assertAllClose(np.array(knp.Cross()(x1, y1)), np.cross(x1, y1))
        self.assertAllClose(np.array(knp.Cross()(x1, y2)), np.cross(x1, y2))
        self.assertAllClose(np.array(knp.Cross()(x1, y3)), np.cross(x1, y3))
        self.assertAllClose(np.array(knp.Cross()(x2, y3)), np.cross(x2, y3))

    def test_full_like(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.full_like(x, 2)), np.full_like(x, 2))
        self.assertAllClose(
            np.array(knp.full_like(x, np.ones([2, 3]))),
            np.full_like(x, np.ones([2, 3])),
        )
        self.assertAllClose(
            np.array(knp.full_like(x, 2, dtype="float32")),
            np.full_like(x, 2, dtype="float32"),
        )

        self.assertAllClose(np.array(knp.FullLike()(x, 2)), np.full_like(x, 2))
        self.assertAllClose(
            np.array(knp.FullLike()(x, np.ones([2, 3]))),
            np.full_like(x, np.ones([2, 3])),
        )
        self.assertAllClose(
            np.array(knp.FullLike()(x, 2, dtype="float32")),
            np.full_like(x, 2, dtype="float32"),
        )

    def test_greater(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(np.array(knp.greater(x, y)), np.greater(x, y))
        self.assertAllClose(np.array(knp.greater(x, 2)), np.greater(x, 2))
        self.assertAllClose(np.array(knp.greater(2, x)), np.greater(2, x))

        self.assertAllClose(np.array(knp.Greater()(x, y)), np.greater(x, y))
        self.assertAllClose(np.array(knp.Greater()(x, 2)), np.greater(x, 2))
        self.assertAllClose(np.array(knp.Greater()(2, x)), np.greater(2, x))

    def test_greater_equal(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(
            np.array(knp.greater_equal(x, y)),
            np.greater_equal(x, y),
        )
        self.assertAllClose(
            np.array(knp.greater_equal(x, 2)),
            np.greater_equal(x, 2),
        )
        self.assertAllClose(
            np.array(knp.greater_equal(2, x)),
            np.greater_equal(2, x),
        )

        self.assertAllClose(
            np.array(knp.GreaterEqual()(x, y)),
            np.greater_equal(x, y),
        )
        self.assertAllClose(
            np.array(knp.GreaterEqual()(x, 2)),
            np.greater_equal(x, 2),
        )
        self.assertAllClose(
            np.array(knp.GreaterEqual()(2, x)),
            np.greater_equal(2, x),
        )

    def test_isclose(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [3, 2, 1]])
        self.assertAllClose(np.array(knp.isclose(x, y)), np.isclose(x, y))
        self.assertAllClose(np.array(knp.isclose(x, 2)), np.isclose(x, 2))
        self.assertAllClose(np.array(knp.isclose(2, x)), np.isclose(2, x))

        self.assertAllClose(np.array(knp.Isclose()(x, y)), np.isclose(x, y))
        self.assertAllClose(np.array(knp.Isclose()(x, 2)), np.isclose(x, 2))
        self.assertAllClose(np.array(knp.Isclose()(2, x)), np.isclose(2, x))


class NumpyOneInputOpsCorrectnessTest(testing.TestCase):
    def test_mean(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.mean(x)), np.mean(x))
        self.assertAllClose(np.array(knp.mean(x, axis=1)), np.mean(x, axis=1))
        self.assertAllClose(
            np.array(knp.mean(x, axis=1, keepdims=True)),
            np.mean(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.Mean()(x)), np.mean(x))
        self.assertAllClose(np.array(knp.Mean(axis=1)(x)), np.mean(x, axis=1))
        self.assertAllClose(
            np.array(knp.Mean(axis=1, keepdims=True)(x)),
            np.mean(x, axis=1, keepdims=True),
        )

    def test_all(self):
        x = np.array([[True, False, True], [True, True, True]])
        self.assertAllClose(np.array(knp.all(x)), np.all(x))
        self.assertAllClose(np.array(knp.all(x, axis=1)), np.all(x, axis=1))
        self.assertAllClose(
            np.array(knp.all(x, axis=1, keepdims=True)),
            np.all(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.All()(x)), np.all(x))
        self.assertAllClose(np.array(knp.All(axis=1)(x)), np.all(x, axis=1))
        self.assertAllClose(
            np.array(knp.All(axis=1, keepdims=True)(x)),
            np.all(x, axis=1, keepdims=True),
        )

    def test_var(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.var(x)), np.var(x))
        self.assertAllClose(np.array(knp.var(x, axis=1)), np.var(x, axis=1))
        self.assertAllClose(
            np.array(knp.var(x, axis=1, keepdims=True)),
            np.var(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.Var()(x)), np.var(x))
        self.assertAllClose(np.array(knp.Var(axis=1)(x)), np.var(x, axis=1))
        self.assertAllClose(
            np.array(knp.Var(axis=1, keepdims=True)(x)),
            np.var(x, axis=1, keepdims=True),
        )

    def test_sum(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.sum(x)), np.sum(x))
        self.assertAllClose(np.array(knp.sum(x, axis=1)), np.sum(x, axis=1))
        self.assertAllClose(
            np.array(knp.sum(x, axis=1, keepdims=True)),
            np.sum(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.Sum()(x)), np.sum(x))
        self.assertAllClose(np.array(knp.Sum(axis=1)(x)), np.sum(x, axis=1))
        self.assertAllClose(
            np.array(knp.Sum(axis=1, keepdims=True)(x)),
            np.sum(x, axis=1, keepdims=True),
        )

    def test_amax(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.amax(x)), np.amax(x))
        self.assertAllClose(np.array(knp.amax(x, axis=1)), np.amax(x, axis=1))
        self.assertAllClose(
            np.array(knp.amax(x, axis=1, keepdims=True)),
            np.amax(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.Amax()(x)), np.amax(x))
        self.assertAllClose(np.array(knp.Amax(axis=1)(x)), np.amax(x, axis=1))
        self.assertAllClose(
            np.array(knp.Amax(axis=1, keepdims=True)(x)),
            np.amax(x, axis=1, keepdims=True),
        )

    def test_amin(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.amin(x)), np.amin(x))
        self.assertAllClose(np.array(knp.amin(x, axis=1)), np.amin(x, axis=1))
        self.assertAllClose(
            np.array(knp.amin(x, axis=1, keepdims=True)),
            np.amin(x, axis=1, keepdims=True),
        )

        self.assertAllClose(np.array(knp.Amin()(x)), np.amin(x))
        self.assertAllClose(np.array(knp.Amin(axis=1)(x)), np.amin(x, axis=1))
        self.assertAllClose(
            np.array(knp.Amin(axis=1, keepdims=True)(x)),
            np.amin(x, axis=1, keepdims=True),
        )

    def test_square(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.square(x)), np.square(x))

        self.assertAllClose(np.array(knp.Square()(x)), np.square(x))

    def test_negative(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.negative(x)), np.negative(x))

        self.assertAllClose(np.array(knp.Negative()(x)), np.negative(x))

    def test_abs(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.abs(x)), np.abs(x))

        self.assertAllClose(np.array(knp.Abs()(x)), np.abs(x))

    def test_absolute(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.absolute(x)), np.absolute(x))

        self.assertAllClose(np.array(knp.Absolute()(x)), np.absolute(x))

    def test_squeeze(self):
        x = np.ones([1, 2, 3, 4, 5])
        self.assertAllClose(np.array(knp.squeeze(x)), np.squeeze(x))
        self.assertAllClose(
            np.array(knp.squeeze(x, axis=0)), np.squeeze(x, axis=0)
        )

        self.assertAllClose(np.array(knp.Squeeze()(x)), np.squeeze(x))
        self.assertAllClose(
            np.array(knp.Squeeze(axis=0)(x)), np.squeeze(x, axis=0)
        )

    def test_transpose(self):
        x = np.ones([1, 2, 3, 4, 5])
        self.assertAllClose(np.array(knp.transpose(x)), np.transpose(x))
        self.assertAllClose(
            np.array(knp.transpose(x, axes=(1, 0, 3, 2, 4))),
            np.transpose(x, axes=(1, 0, 3, 2, 4)),
        )

        self.assertAllClose(np.array(knp.Transpose()(x)), np.transpose(x))
        self.assertAllClose(
            np.array(knp.Transpose(axes=(1, 0, 3, 2, 4))(x)),
            np.transpose(x, axes=(1, 0, 3, 2, 4)),
        )

    def test_arcos(self):
        x = np.array([[1, 0.5, -0.7], [0.9, 0.2, -1]])
        self.assertAllClose(np.array(knp.arccos(x)), np.arccos(x))

        self.assertAllClose(np.array(knp.Arccos()(x)), np.arccos(x))

    def test_arcsin(self):
        x = np.array([[1, 0.5, -0.7], [0.9, 0.2, -1]])
        self.assertAllClose(np.array(knp.arcsin(x)), np.arcsin(x))

        self.assertAllClose(np.array(knp.Arcsin()(x)), np.arcsin(x))

    def test_argmax(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.argmax(x)), np.argmax(x))
        self.assertAllClose(
            np.array(knp.argmax(x, axis=1)), np.argmax(x, axis=1)
        )

        self.assertAllClose(np.array(knp.Argmax()(x)), np.argmax(x))
        self.assertAllClose(
            np.array(knp.Argmax(axis=1)(x)), np.argmax(x, axis=1)
        )

    def test_argmin(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.argmin(x)), np.argmin(x))
        self.assertAllClose(
            np.array(knp.argmin(x, axis=1)), np.argmin(x, axis=1)
        )

        self.assertAllClose(np.array(knp.Argmin()(x)), np.argmin(x))
        self.assertAllClose(
            np.array(knp.Argmin(axis=1)(x)), np.argmin(x, axis=1)
        )

    def test_argsort(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.argsort(x)), np.argsort(x))
        self.assertAllClose(
            np.array(knp.argsort(x, axis=1)), np.argsort(x, axis=1)
        )
        self.assertAllClose(
            np.array(knp.argsort(x, axis=None)),
            np.argsort(x, axis=None),
        )

        self.assertAllClose(np.array(knp.Argsort()(x)), np.argsort(x))
        self.assertAllClose(
            np.array(knp.Argsort(axis=1)(x)), np.argsort(x, axis=1)
        )
        self.assertAllClose(
            np.array(knp.Argsort(axis=None)(x)),
            np.argsort(x, axis=None),
        )

    def test_array(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.array(x)), np.array(x))
        self.assertAllClose(np.array(knp.Array()(x)), np.array(x))

    def test_average(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        weights = np.ones([2, 3])
        weights_1d = np.ones([3])
        self.assertAllClose(np.array(knp.average(x)), np.average(x))
        self.assertAllClose(
            np.array(knp.average(x, axis=1)), np.average(x, axis=1)
        )
        self.assertAllClose(
            np.array(knp.average(x, axis=1, weights=weights)),
            np.average(x, axis=1, weights=weights),
        )
        self.assertAllClose(
            np.array(knp.average(x, axis=1, weights=weights_1d)),
            np.average(x, axis=1, weights=weights_1d),
        )

        self.assertAllClose(np.array(knp.Average()(x)), np.average(x))
        self.assertAllClose(
            np.array(knp.Average(axis=1)(x)), np.average(x, axis=1)
        )
        self.assertAllClose(
            np.array(knp.Average(axis=1)(x, weights=weights)),
            np.average(x, axis=1, weights=weights),
        )
        self.assertAllClose(
            np.array(knp.Average(axis=1)(x, weights=weights_1d)),
            np.average(x, axis=1, weights=weights_1d),
        )

    def test_broadcast_to(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(
            np.array(knp.broadcast_to(x, [2, 2, 3])),
            np.broadcast_to(x, [2, 2, 3]),
        )

        self.assertAllClose(
            np.array(knp.BroadcastTo([2, 2, 3])(x)),
            np.broadcast_to(x, [2, 2, 3]),
        )

    def test_ceil(self):
        x = np.array([[1.2, 2.1, -2.5], [2.4, -11.9, -5.5]])
        self.assertAllClose(np.array(knp.ceil(x)), np.ceil(x))
        self.assertAllClose(np.array(knp.Ceil()(x)), np.ceil(x))

    def test_clip(self):
        x = np.array([[1.2, 2.1, -2.5], [2.4, -11.9, -5.5]])
        self.assertAllClose(np.array(knp.clip(x, -2, 2)), np.clip(x, -2, 2))
        self.assertAllClose(np.array(knp.clip(x, -2, 2)), np.clip(x, -2, 2))

        self.assertAllClose(np.array(knp.Clip(0, 1)(x)), np.clip(x, 0, 1))
        self.assertAllClose(np.array(knp.Clip(0, 1)(x)), np.clip(x, 0, 1))

    def test_concatenate(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [6, 5, 4]])
        z = np.array([[7, 8, 9], [9, 8, 7]])
        self.assertAllClose(
            np.array(knp.concatenate([x, y], axis=0)),
            np.concatenate([x, y], axis=0),
        )
        self.assertAllClose(
            np.array(knp.concatenate([x, y, z], axis=0)),
            np.concatenate([x, y, z], axis=0),
        )
        self.assertAllClose(
            np.array(knp.concatenate([x, y], axis=1)),
            np.concatenate([x, y], axis=1),
        )

        self.assertAllClose(
            np.array(knp.Concatenate(axis=0)([x, y])),
            np.concatenate([x, y], axis=0),
        )
        self.assertAllClose(
            np.array(knp.Concatenate(axis=0)([x, y, z])),
            np.concatenate([x, y, z], axis=0),
        )
        self.assertAllClose(
            np.array(knp.Concatenate(axis=1)([x, y])),
            np.concatenate([x, y], axis=1),
        )

    def test_conjugate(self):
        x = np.array([[1 + 2j, 2 + 3j], [3 + 4j, 4 + 5j]])
        self.assertAllClose(np.array(knp.conjugate(x)), np.conjugate(x))
        self.assertAllClose(np.array(knp.Conjugate()(x)), np.conjugate(x))

    def test_conj(self):
        x = np.array([[1 + 2j, 2 + 3j], [3 + 4j, 4 + 5j]])
        self.assertAllClose(np.array(knp.conj(x)), np.conj(x))
        self.assertAllClose(np.array(knp.Conj()(x)), np.conj(x))

    def test_copy(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.copy(x)), np.copy(x))
        self.assertAllClose(np.array(knp.Copy()(x)), np.copy(x))

    def test_cos(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.cos(x)), np.cos(x))
        self.assertAllClose(np.array(knp.Cos()(x)), np.cos(x))

    def test_count_nonzero(self):
        x = np.array([[0, 2, 3], [3, 2, 0]])
        self.assertAllClose(np.array(knp.count_nonzero(x)), np.count_nonzero(x))
        self.assertAllClose(
            np.array(knp.count_nonzero(x, axis=1)),
            np.count_nonzero(x, axis=1),
        )

        self.assertAllClose(
            np.array(knp.CountNonzero()(x)),
            np.count_nonzero(x),
        )
        self.assertAllClose(
            np.array(knp.CountNonzero(axis=1)(x)),
            np.count_nonzero(x, axis=1),
        )

    def test_cumprod(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.cumprod(x)), np.cumprod(x))
        self.assertAllClose(
            np.array(knp.cumprod(x, axis=0)),
            np.cumprod(x, axis=0),
        )
        self.assertAllClose(
            np.array(knp.cumprod(x, axis=None)),
            np.cumprod(x, axis=None),
        )

        self.assertAllClose(np.array(knp.Cumprod()(x)), np.cumprod(x))
        self.assertAllClose(
            np.array(knp.Cumprod(axis=0)(x)),
            np.cumprod(x, axis=0),
        )
        self.assertAllClose(
            np.array(knp.Cumprod(axis=None)(x)),
            np.cumprod(x, axis=None),
        )

    def test_cumsum(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.cumsum(x)), np.cumsum(x))
        self.assertAllClose(
            np.array(knp.cumsum(x, axis=0)),
            np.cumsum(x, axis=0),
        )
        self.assertAllClose(
            np.array(knp.cumsum(x, axis=1)),
            np.cumsum(x, axis=1),
        )

        self.assertAllClose(np.array(knp.Cumsum()(x)), np.cumsum(x))
        self.assertAllClose(
            np.array(knp.Cumsum(axis=0)(x)),
            np.cumsum(x, axis=0),
        )
        self.assertAllClose(
            np.array(knp.Cumsum(axis=1)(x)),
            np.cumsum(x, axis=1),
        )

    def test_diag(self):
        x = np.array([1, 2, 3])
        self.assertAllClose(np.array(knp.diag(x)), np.diag(x))
        self.assertAllClose(np.array(knp.diag(x, k=1)), np.diag(x, k=1))
        self.assertAllClose(np.array(knp.diag(x, k=-1)), np.diag(x, k=-1))

        self.assertAllClose(np.array(knp.Diag()(x)), np.diag(x))
        self.assertAllClose(np.array(knp.Diag(k=1)(x)), np.diag(x, k=1))
        self.assertAllClose(np.array(knp.Diag(k=-1)(x)), np.diag(x, k=-1))

        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.diag(x)), np.diag(x))
        self.assertAllClose(np.array(knp.diag(x, k=1)), np.diag(x, k=1))
        self.assertAllClose(np.array(knp.diag(x, k=-1)), np.diag(x, k=-1))

        self.assertAllClose(np.array(knp.Diag()(x)), np.diag(x))
        self.assertAllClose(np.array(knp.Diag(k=1)(x)), np.diag(x, k=1))
        self.assertAllClose(np.array(knp.Diag(k=-1)(x)), np.diag(x, k=-1))

    def test_diagonal(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.diagonal(x)), np.diagonal(x))
        self.assertAllClose(
            np.array(knp.diagonal(x, offset=1)),
            np.diagonal(x, offset=1),
        )
        self.assertAllClose(
            np.array(knp.diagonal(x, offset=-1)), np.diagonal(x, offset=-1)
        )

        self.assertAllClose(np.array(knp.Diagonal()(x)), np.diagonal(x))
        self.assertAllClose(
            np.array(knp.Diagonal(offset=1)(x)), np.diagonal(x, offset=1)
        )
        self.assertAllClose(
            np.array(knp.Diagonal(offset=-1)(x)), np.diagonal(x, offset=-1)
        )

        x = np.ones([2, 3, 4, 5])
        self.assertAllClose(np.array(knp.diagonal(x)), np.diagonal(x))
        self.assertAllClose(
            np.array(knp.diagonal(x, offset=1, axis1=2, axis2=3)),
            np.diagonal(x, offset=1, axis1=2, axis2=3),
        )
        self.assertAllClose(
            np.array(knp.diagonal(x, offset=-1, axis1=2, axis2=3)),
            np.diagonal(x, offset=-1, axis1=2, axis2=3),
        )

    def test_exp(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.exp(x)), np.exp(x))
        self.assertAllClose(np.array(knp.Exp()(x)), np.exp(x))

    def test_expand_dims(self):
        x = np.ones([2, 3, 4])
        self.assertAllClose(
            np.array(knp.expand_dims(x, 0)), np.expand_dims(x, 0)
        )
        self.assertAllClose(
            np.array(knp.expand_dims(x, 1)), np.expand_dims(x, 1)
        )
        self.assertAllClose(
            np.array(knp.expand_dims(x, -2)), np.expand_dims(x, -2)
        )

        self.assertAllClose(
            np.array(knp.ExpandDims(0)(x)), np.expand_dims(x, 0)
        )
        self.assertAllClose(
            np.array(knp.ExpandDims(1)(x)), np.expand_dims(x, 1)
        )
        self.assertAllClose(
            np.array(knp.ExpandDims(-2)(x)), np.expand_dims(x, -2)
        )

    def test_expm1(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.expm1(x)), np.expm1(x))
        self.assertAllClose(np.array(knp.Expm1()(x)), np.expm1(x))

    def test_flip(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        self.assertAllClose(np.array(knp.flip(x)), np.flip(x))
        self.assertAllClose(np.array(knp.flip(x, 0)), np.flip(x, 0))
        self.assertAllClose(np.array(knp.flip(x, 1)), np.flip(x, 1))

        self.assertAllClose(np.array(knp.Flip()(x)), np.flip(x))
        self.assertAllClose(np.array(knp.Flip(0)(x)), np.flip(x, 0))
        self.assertAllClose(np.array(knp.Flip(1)(x)), np.flip(x, 1))

    def test_floor(self):
        x = np.array([[1.1, 2.2, -3.3], [3.3, 2.2, -1.1]])
        self.assertAllClose(np.array(knp.floor(x)), np.floor(x))
        self.assertAllClose(np.array(knp.Floor()(x)), np.floor(x))

    def test_hstack(self):
        x = np.array([[1, 2, 3], [3, 2, 1]])
        y = np.array([[4, 5, 6], [6, 5, 4]])
        self.assertAllClose(np.array(knp.hstack([x, y])), np.hstack([x, y]))
        self.assertAllClose(np.array(knp.Hstack()([x, y])), np.hstack([x, y]))

        x = np.ones([2, 3, 4])
        y = np.ones([2, 5, 4])
        self.assertAllClose(np.array(knp.hstack([x, y])), np.hstack([x, y]))
        self.assertAllClose(np.array(knp.Hstack()([x, y])), np.hstack([x, y]))

    def test_imag(self):
        x = np.array([[1 + 1j, 2 + 2j, 3 + 3j], [3 + 3j, 2 + 2j, 1 + 1j]])
        self.assertAllClose(np.array(knp.imag(x)), np.imag(x))
        self.assertAllClose(np.array(knp.Imag()(x)), np.imag(x))

    def test_isfinite(self):
        x = np.array([[1, 2, np.inf], [np.nan, np.nan, np.nan]])
        self.assertAllClose(np.array(knp.isfinite(x)), np.isfinite(x))
        self.assertAllClose(np.array(knp.Isfinite()(x)), np.isfinite(x))

    def test_isinf(self):
        x = np.array([[1, 2, np.inf], [np.nan, np.nan, np.nan]])
        self.assertAllClose(np.array(knp.isinf(x)), np.isinf(x))
        self.assertAllClose(np.array(knp.Isinf()(x)), np.isinf(x))

    def test_isnan(self):
        x = np.array([[1, 2, np.inf], [np.nan, np.nan, np.nan]])
        self.assertAllClose(np.array(knp.isnan(x)), np.isnan(x))
        self.assertAllClose(np.array(knp.Isnan()(x)), np.isnan(x))


class NumpyArrayCreateOpsCorrectnessTest(testing.TestCase):
    def test_ones(self):
        self.assertAllClose(np.array(knp.ones([2, 3])), np.ones([2, 3]))
        self.assertAllClose(np.array(knp.Ones()([2, 3])), np.ones([2, 3]))

    def test_zeros(self):
        self.assertAllClose(np.array(knp.zeros([2, 3])), np.zeros([2, 3]))
        self.assertAllClose(np.array(knp.Zeros()([2, 3])), np.zeros([2, 3]))

    def test_eye(self):
        self.assertAllClose(np.array(knp.eye(3)), np.eye(3))
        self.assertAllClose(np.array(knp.eye(3, 4)), np.eye(3, 4))
        self.assertAllClose(np.array(knp.eye(3, 4, 1)), np.eye(3, 4, 1))

        self.assertAllClose(np.array(knp.Eye()(3)), np.eye(3))
        self.assertAllClose(np.array(knp.Eye()(3, 4)), np.eye(3, 4))
        self.assertAllClose(np.array(knp.Eye()(3, 4, 1)), np.eye(3, 4, 1))

    def test_arange(self):
        self.assertAllClose(np.array(knp.arange(3)), np.arange(3))
        self.assertAllClose(np.array(knp.arange(3, 7)), np.arange(3, 7))
        self.assertAllClose(np.array(knp.arange(3, 7, 2)), np.arange(3, 7, 2))

        self.assertAllClose(np.array(knp.Arange()(3)), np.arange(3))
        self.assertAllClose(np.array(knp.Arange()(3, 7)), np.arange(3, 7))
        self.assertAllClose(np.array(knp.Arange()(3, 7, 2)), np.arange(3, 7, 2))

    def test_full(self):
        self.assertAllClose(np.array(knp.full([2, 3], 0)), np.full([2, 3], 0))
        self.assertAllClose(
            np.array(knp.full([2, 3], 0.1)), np.full([2, 3], 0.1)
        )
        self.assertAllClose(
            np.array(knp.full([2, 3], [1, 4, 5])), np.full([2, 3], [1, 4, 5])
        )

        self.assertAllClose(np.array(knp.Full()([2, 3], 0)), np.full([2, 3], 0))
        self.assertAllClose(
            np.array(knp.Full()([2, 3], 0.1)), np.full([2, 3], 0.1)
        )
        self.assertAllClose(
            np.array(knp.Full()([2, 3], [1, 4, 5])), np.full([2, 3], [1, 4, 5])
        )

    def test_identity(self):
        self.assertAllClose(np.array(knp.identity(3)), np.identity(3))
        self.assertAllClose(np.array(knp.Identity()(3)), np.identity(3))
