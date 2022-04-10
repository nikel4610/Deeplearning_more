import csv
import numpy as np
import simple_SLP

def relu(x): # 원솟값과 0을 비교해서 작지 않은 쪽 고름
    return np.maximum(x, 0) # max 아님 maximum 이 맞음

def sigmoid(x):
    return np.exp(-relu(-x)) / (1.0 + np.exp(-np.abs(x)))

def sigmoid_derv(x, y):
    return y * (1 - y)

def sigmoid_cross_entropy_with_logits(z, x):
    return relu(x) - x * z + np.log(1 + np.exp(-np.abs(x)))

def sigmoid_cross_entropy_with_logits_derv(z, x):
    return -z + sigmoid(x)

def eval_accuracy(output, y): # 정확도 계산
    estimate = np.greater(output, 0)
    answer = np.greater(y, 0.5) # 원래는 1 과 0 이지만 안전하게 0.5로 비교
    correct = np.equal(estimate, answer) # 연산 수행하면 결국 1, 0으로 간주해 계산하므로 올바른 판단의 비율 구해짐

    return np.mean(correct)

def forward_postproc(output, y): # 순전파 처리
    entropy = sigmoid_cross_entropy_with_logits(y, output) # 시그모이드 교차 엔트로피
    loss = np.mean(entropy) # 평균으로 loss값 계산
    return loss, [y, output, entropy]

def backprop_postproc(G_loss, aux): # 역전파 처리
    y, output, entropy = aux

    g_loss_entropy = 1.0 / np.prod(entropy.shape) # 각 원소의 손실 기울기로 부여
    g_entropy_output = sigmoid_cross_entropy_with_logits_derv(y, output)

    G_entropy = g_loss_entropy * G_loss
    G_output = g_entropy_output * G_entropy

    return G_output

def load_pulsar_dataset():
    with open("D:/python_project/nalcoding/Datasets/pulsar_data_test.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        rows = []
        for row in csvreader:
            rows.append(row)
    global data, input_cnt, output_cnt
    input_cnt, output_cnt = 8, 1
    data = np.array(rows, dtype='float32')

def pulsar_exec(epoch_count = 10, mb_size = 10, report = 1):
    load_pulsar_dataset()
    simple_SLP.init_model()
    simple_SLP.train_and_test(epoch_count, mb_size, report)
