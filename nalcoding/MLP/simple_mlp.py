import numpy as np

RND_MEAN = 0 # 정규분포 평균
RND_STD = 0.0030 # 정규분포 표준편차

LEARNING_RATE = 0.001 # 학습률
# 학습률 다양하게 바꾸어 가며 실행 가능

def set_hidden(info):
    global hidden_cnt, hidden_config
    if isinstance(info, int):
        hidden_cnt = info
        hidden_config = None
    else:
        hidden_config = info

global hidden_config

def init_model():
    if hidden_config is not None:
        print('은닉 계층 {}개를 갖는 다층 퍼셉트론.'.format(len(hidden_config)))
        init_model_hiddens()
    else:
        print('은닉 계층을 하나를 갖는 다층 퍼셉트론.')
        init_model_hidden1()

def forward_neuralnet(x):
    if hidden_config is not None:
        return forward_neuralnet_hiddens(x)
    else:
        return forward_neuralnet_hidden1(x)

def backprop_neuralnet(G_output, hiddens):
    if hidden_config is not None:
        backprop_neuralnet_hiddens(G_output, hiddens)
    else:
        backprop_neuralnet_hidden(G_output, hiddens)

def backprop_neuralnet_hiddens(G_output, aux):
    global pm_output, pm_hiddens

    hiddens = aux

    G_output_w_out = hiddens[-1].transpose()
    G_w_out = np.matmul(G_output_w_out, G_output)
    G_b_out = np.sum(G_output, axis = 0)

    g_output_hidden = pm_output['w'].transpose()
    G_hidden = np.matmul(G_output, g_output_hidden)

    for n in reversed(range(len(pm_hiddens))):
        G_hidden = G_hidden * relu_derv(hiddens[n+1])

        g_hidden_w_hid = hiddens[n].transpose()
        G_w_hid = np.matmul(g_hidden_w_hid, G_hidden)
        G_b_hid = np.sum(G_hidden, axis = 0)

        g_hidden_hidden = pm_hiddens[n]['w'].transpose()
        G_hidden = np.matmul(G_hidden, g_hidden_hidden)

        pm_hiddens[n]['w'] -= LEARNING_RATE * G_w_hid
        pm_hiddens[n]['b'] -= LEARNING_RATE * G_b_hid

def forward_neuralnet_hiddens(x):
    global pm_output, pm_hiddens

    hidden = x
    hiddens = [x]

    for pm_hidden in pm_hiddens:
        hidden = relu(np.matmul(hidden, pm_hidden['w']) + pm_hidden['b'])
        hiddens.append(hidden)

    output = np.matmul(hidden, pm_output['w']) + pm_output['b']

    return output, hiddens

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