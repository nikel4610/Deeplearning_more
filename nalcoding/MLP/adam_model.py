import mlp_model
import math_util
import numpy as np

class AdamModel(mlp_model.MLPModel):
    def __init__ (self, name, dataset, hconfigs):
        self.use_adam = False # 메서드 호출 전에 True로 변경
        super(AdamModel, self).__init__(name, dataset, hconfigs)

def adam_backprop_layer(self, G_y, hconfig, pm, aux):
    x, y = aux

    if hconfig is not None: G_y = math_util.relu_derv(y) * G_y

    g_y_weight = x.transpose()
    g_y_input = pm['w'].transpose()

    G_weight = np.matmul(g_y_weight, G_y)
    G_bias = np.sum(G_y, axis=0)
    G_input = np.matmul(G_y, g_y_input)

    self.update_param(pm, 'w', G_weight)
    self.update_param(pm, 'b', G_bias)

    return G_input

AdamModel.backprop_layer = adam_backprop_layer


def adam_update_param(self, pm, key, delta):
    if self.use_adam:
        delta = self.eval_adam_delta(pm, key, delta)

    pm[key] -= self.learning_rate * delta

AdamModel.update_param = adam_update_param


