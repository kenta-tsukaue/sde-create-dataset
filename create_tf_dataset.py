"""Return training and evaluation/test datasets from config files."""
import jax
import tensorflow as tf
import tensorflow_datasets as tfds

import tf_datasets.data_set

ds = tfds.load("data_set")
print(ds)
