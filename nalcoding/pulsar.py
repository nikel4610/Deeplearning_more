import csv
import numpy as np

def forward_postproc(output, y): # 순전파 처리
    entropy = sigmoid_cross_entropy_with_logits(y, output) # 시그모이드 교차 엔트로피
    loss = np.mean(entropy) # 평균으로 loss값 계산
    return loss, [y, output, entropy]

def backdrop_postproc(G_loss, aux): # 역전파 처리
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

def pulsar_exec(epoch_count = 10, mb_size = 10, report = 1)
    load_pulsar_dataset()
    init_model()
    train_and_test(epoch_count, mb_size, report)