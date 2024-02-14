# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
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
"""Distribution tests for keras.layers.preprocessing.text_vectorization."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf

import numpy as np

import keras
from keras import keras_parameterized
from keras.distribute.strategy_combinations import all_strategies
from keras.layers.preprocessing import preprocessing_test_utils
from keras.layers.preprocessing import text_vectorization
from keras.layers.preprocessing import text_vectorization_v1


def get_layer_class():
  if tf.executing_eagerly():
    return text_vectorization.TextVectorization
  else:
    return text_vectorization_v1.TextVectorization


@tf.__internal__.distribute.combinations.generate(
    tf.__internal__.test.combinations.combine(
        distribution=all_strategies,
        mode=["eager", "graph"]))
class TextVectorizationDistributionTest(
    keras_parameterized.TestCase,
    preprocessing_test_utils.PreprocessingLayerTest):

  def test_distribution_strategy_output(self, distribution):
    vocab_data = ["earth", "wind", "and", "fire"]
    input_array = np.array([["earth", "wind", "and", "fire"],
                            ["fire", "and", "earth", "michigan"]])
    input_dataset = tf.data.Dataset.from_tensor_slices(input_array).batch(
        2, drop_remainder=True)

    expected_output = [[2, 3, 4, 5], [5, 4, 2, 1]]

    tf.config.set_soft_device_placement(True)

    with distribution.scope():
      input_data = keras.Input(shape=(None,), dtype=tf.string)
      layer = get_layer_class()(
          max_tokens=None,
          standardize=None,
          split=None,
          output_mode=text_vectorization.INT)
      layer.set_vocabulary(vocab_data)
      int_data = layer(input_data)
      model = keras.Model(inputs=input_data, outputs=int_data)

    output_dataset = model.predict(input_dataset)
    self.assertAllEqual(expected_output, output_dataset)

  def test_distribution_strategy_output_with_adapt(self, distribution):
    vocab_data = [[
        "earth", "earth", "earth", "earth", "wind", "wind", "wind", "and",
        "and", "fire"
    ]]
    vocab_dataset = tf.data.Dataset.from_tensors(vocab_data)
    input_array = np.array([["earth", "wind", "and", "fire"],
                            ["fire", "and", "earth", "michigan"]])
    input_dataset = tf.data.Dataset.from_tensor_slices(input_array).batch(
        2, drop_remainder=True)

    expected_output = [[2, 3, 4, 5], [5, 4, 2, 1]]

    tf.config.set_soft_device_placement(True)

    with distribution.scope():
      input_data = keras.Input(shape=(None,), dtype=tf.string)
      layer = get_layer_class()(
          max_tokens=None,
          standardize=None,
          split=None,
          output_mode=text_vectorization.INT)
      layer.adapt(vocab_dataset)
      int_data = layer(input_data)
      model = keras.Model(inputs=input_data, outputs=int_data)

    output_dataset = model.predict(input_dataset)
    self.assertAllEqual(expected_output, output_dataset)
if __name__ == "__main__":
  tf.test.main()
