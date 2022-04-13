import numpy as np

def relu (x):
    return np.maximum(x, 0)

def forward_neuralnet_hidden1(x):
    global pm_output, pm_hidden

    hidden = relu(np.matmul(x, pm_hidden['w']) + pm_hidden['b']) # 은닉 계층
    output = np.matmul(hidden, pm_output['w']) + pm_output['b'] # 출력 계층

    return output, [x, hidden]

def alloc_param_pair(shape):
    weight = np.random.normal(RND_MEAN, RND_STD, shape) # 가중치 행렬
    bias = np.zeros(shape[-1]) # 편항 벡터
    return {'w': weight, 'b': bias} # 가중치 와 편향 나눔


def init_model_hidden1():
    global pm_output, pm_hidden, input_cnt, output_cnt, hidden_cnt

    pm_hidden = alloc_param_pair([input_cnt, hidden_cnt]) # 은닉 계층
    pm_output = alloc_param_pair([hidden_cnt, output_cnt]) # 출력 계층
