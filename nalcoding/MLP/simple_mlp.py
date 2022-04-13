import numpy as np

def init_model_hiddens():
    global pm_output, pm_hiddens, input_cnt, output_cnt, hidden_config

    pm_hiddens = []
    prev_cnt = input_cnt

    for hidden_cnt in hidden_config:
        pm_hiddens.append(alloc_param_pair([prev_cnt, hidden_cnt]))
        prev_cnt = hidden_cnt

    pm_output = alloc_param_pair([prev_cnt, output_cnt])

def relu_derv(y):
    return np.sign(y)

def backprop_neuralnet_hidden(G_output, aux):
    global pm_output, pm_hidden

    x, hidden = aux

    g_output_w_out = hidden.transpose()
    G_w_out = np.matmul(g_output_w_out, G_output)
    G_b_out = np.sum(G_output, axis = 0)

    g_output_hidden = pm_output['w'].transpose()
    G_hidden = np.matmul(G_output, g_output_hidden)

    pm_output['w'] -= LEARNING_RATE * G_w_out
    pm_output['b'] -= LEARNING_RATE * G_b_out

    G_hidden = G_hidden * relu_derv(hidden)

    g_hidden_w_hid = x.transpose()
    G_w_hid = np.matmul(g_hidden_w_hid, G_hidden)
    G_b_hid = np.sum(G_hidden, axis = 0)

    pm_hidden['w'] -= LEARNING_RATE * G_w_hid
    pm_hidden['b'] -= LEARNING_RATE * G_b_hid

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
