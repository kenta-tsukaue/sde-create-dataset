"""data_set dataset."""
import os
import pickle
import tensorflow_datasets as tfds


# TODO(data_set): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(data_set): BibTeX citation
_CITATION = """
"""


class DataSet(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for data_set dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(data_set): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'tensor': tfds.features.Tensor(shape=(32,32,10), dtype="int32"),
            'label': tfds.features.ClassLabel(names=['no', 'yes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('tensor', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(data_set): Downloads the data and defines the splits
    path = "/public/tsukaue/graduation/sde-datas/data_"

    # TODO(data_set): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path + "/train_tensors"),
        'test' : self._generate_examples(path + '/test_tensors')
    }

  def _generate_examples(self, path):
    dir=os.listdir(path)
    """Yields examples."""
    # TODO(data_set): Yields (key, example) tuples from the dataset
    for f in dir:
      with open(path + "/" + f, 'rb') as f:
        pointData = pickle.load(f)
      #print(f.name)

      yield f.name, {
          'tensor': pointData,
          'label': 'yes',
      }