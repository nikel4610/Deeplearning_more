import math_util
import numpy as np
import time

np.random.seed(1234)
def randomize():
    np.random.seed(time.time())

class Model(object):
    def __init__(self, name, dataset):
        self.name = name
        self.dataset = dataset
        self.is_training = False
        if not hasattr(self, 'rand_std'):
            self.rand_std = 0.030

    def __str__(self):
        return '{}/{}'.format(self.name, self.dataset)

    def exec_all(self, epoch_count = 10, batch_size = 10, learning_rate = 0.001,
                 report = 0, show_cnt = 3):
        self.train(epoch_count, batch_size, learning_rate, report)
        self.test()
        if show_cnt > 0:
            self.visualize(show_cnt)

class MlpModel(Model): # 외부에서 함수 정의하고 메서드로 등록
    def __init__(self, name, dataset, hconfigs):
        super(MlpModel, self).__init__(name, dataset)
        self.init_parameters(hconfigs)

def mlp_init_parameters(self, hconfigs):
    self.hconfigs = hconfigs
    self.pm_hiddens = []

    prev_shape = self.dataset.input_shape

    for hconfig in hconfigs:
        pm_hidden, prev_shape = self.alloc_layer_param(prev_shape, hconfig)
        self.pm_hiddens.append(pm_hidden)

    output_cnt = int(np.proc(self.dataset.output_shape))
    self.pm_output, _ = self.alloc_layer_param(prev_shape, output_cnt)

def mp_alloc_layer_param(self, input_shape, hconfig):
    input_cnt = np.proc(input_shape)
    output_cnt = hconfig

    weight, bias = self.alloc_param_pair([input_cnt, output_cnt])

    return {'w': weight, 'b': bias}, output_cnt

def mlp_alloc_param_pair(self, shape):
    weight = np.random.normal(0, self.rand_std, shape)
    bias = np.zeros([shape[-1]])
    return weight, bias

MlpModel.init_parameters = mlp_init_parameters
MlpModel.alloc_layer_param = mp_alloc_layer_param
MlpModel.alloc_param_pair = mlp_alloc_param_pair

def mlp_model_train(self, epoch_count = 10, batch_size = 10,
                    learning_rate = 0.001, report = 0):
    self.learning_rate = learning_rate

    batch_count = int(self.dataset.train_count / batch_size)
    time1 = time2 = int(time.time())
    if report != 0:
        print('Model {} train started:'.format(self.name))

    for epoch in range(epoch_count):
        costs = []
        accs = []
        self.dataset.shuffle_train_data(batch_size*batch_count) # 데이터 뒤섞기 기능 따로 실행
        for n in range(batch_count):
            trX, trY = self.dataset.get_train_data(batch_size, n)
            cost, acc = self.train_step(trX, trY)
            costs.append(cost)
            accs.append(acc)

    if report > 0 and (epoch + 1) % report == 0:
        vaX, vaY = self.dataset.get_validate_data(100)
        acc = self.eval_accuracy(vaX, vaY)
        time3 = int(time.time())
        tm1, tm2 = time3-time2, time3-time1
        self.dataset.train_prt_result(epoch + 1, costs, accs, acc, tm1, tm2)
        time2 = time3

    tm_total = int(time.time()) - time1
    print('Model {} train ended in {} secs'.format(self.name, tm_total))

MlpModel.train = mlp_model_train