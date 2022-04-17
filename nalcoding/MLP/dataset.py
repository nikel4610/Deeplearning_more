import math_util
import numpy as np

class Dataset(object):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __str__(self):
        return '{}({}, {}+{}+{})'.format(self.name, self.mode,
                                         len(self.tr_xs), len(self.te_xs), len(self.va_xs))

    @property
    def train_count(self):
        return len(self.tr_xs)

def dataset_get_train_data(self, batch_size, nth):
    from_idx = nth * batch_size
    to_idx = (nth + 1) * batch_size

    tr_X = self.tr_xs[self.indices[from_idx:to_idx]]
    tr_Y = self.tr_ys[self.indices[from_idx:to_idx]]

    return tr_X, tr_Y

def dataset_shuffle_train_data(self, size):
    self.indices = np.arange(size)
    np.random.shuffle(self.indices)

Dataset.get_train_data = dataset_get_train_data
Dataset.shuffle_train_data = dataset_shuffle_train_data

def dataset_get_test_data(self):
    return self.te_xs, self.te_ys

Dataset.get_test_data = dataset_get_test_data

def dataset_get_validate_data(self, count):
    self.va_indices = np.arange(len(self.va_xs)) # self.indices 와 관계 없음
    np.random.shuffle(self.va_indices)

    va_X = self.va_xs[self.va_indices[0:count]]
    va_Y = self.va_ys[self.va_indices[0:count]]

    return va_X, va_Y

Dataset.get_validate_data = dataset_get_validate_data
Dataset.get_visualize_data = dataset_get_validate_data