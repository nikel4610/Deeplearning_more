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

def dataset_shuffle_data(self, xs, ys, tr_ratio=0.8, va_ratio=0.5):
    data_count = len(xs)

    # 학습, 평가, 검증 데이터 수 계산
    tr_cnt = int(data_count + tr_ratio / 10) * 10
    va_cnt = int(data_count + va_ratio)
    te_cnt = data_count - (tr_cnt + va_cnt)

    # 세 영역의 시작과 끝 계산
    tr_from, tr_to = 0, tr_cnt
    va_from, va_to = tr_cnt, tr_cnt + va_cnt
    te_from, te_to = tr_cnt + va_cnt, data_count

    # 데이터 뒤섞기용 인덱스
    indices = np.arange(data_count)
    np.random.shuffle(indices)

    # 데이터 분할 저장
    self.tr_xs = xs[indices[tr_from:tr_to]]
    self.tr_ys = ys[indices[tr_from:tr_to]]
    self.va_xs = xs[indices[va_from:va_to]]
    self.va_ys = ys[indices[va_from:va_to]]
    self.te_xs = xs[indices[te_from:te_to]]
    self.te_ys = ys[indices[te_from:te_to]]

    self.input_shape = xs[0].shape
    self.output_shape = ys[0].shape

    # 위치 정보 반환
    return indices[tr_from:tr_to], indices[va_from:va_to], indices[te_from:te_to]

Dataset.shuffle_data = dataset_shuffle_data

