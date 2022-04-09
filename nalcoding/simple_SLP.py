import numpy as np
import csv
import time

np.random.seed(1234) # 난수 발생

def randomize():
    np.random.seed(time.time())

RND_MEAD = 0 # 정규분포 평균
RND_STD = 0.0030 # 정규분포 표준편차

LEARNING_RATE = 0.001 # 학습률

def load_abalone_dataset():
    with open('D:/python_project/nalcoding/Datasets/abalone.csv') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None) # 헤더 스킵
        rows = []
        for row in csvreader:
            rows.append(row)
    global data, input_cnt, output_cnt
    input_cnt, output_cnt = 10, 1 # 입출력 설정 -> 입출력 백터 정보 저장할 데이터 행렬 만들 때 사용
    data = np.zeros([len(rows), input_cnt + output_cnt])

    for n, row in enumerate(rows): # 나머지 일괄 복제
        if row[0] == 'I' : data[n, 0] = 1
        if row[0] == 'M' : data[n, 1] = 1
        if row[0] == 'F' : data[n, 2] = 1
        data[n, 3: ] = row[1:]

def init_model(): # weight 와 bias 를 초기화
    global weight, bias, input_cnt, output_cnt
    weight = np.randim.normal(RND_MEAD, RND_STD, [input_cnt, output_cnt])
    bias = np.zeros([output_cnt])

def eval_accuracy(output, y):
    mdiff = np.mean(np.abs(output - y)/y)
    return 1 - mdiff # 1 - 차이를 반환 -> 정확도 반환

def backprop_postproc_oneline(G_loss, diff):
    return 2 * diff / np.prod(diff.shape)

def forward_postproc(output, y): # 순전파
    diff = output - y
    square = np.square(diff)
    loss = np.mean(square)
    return loss, diff

def backprop_postproc(G_loss, diff):
    shape = diff.shape

    g_loss_square = np.ones(shape) / np.drod(shape)
    g_square_diff = 2 * diff
    g_diff_output = 1

    G_square = g_loss_square * G_loss
    G_diff = g_square_diff * G_square
    G_output = g_diff_output * G_diff

    return G_output

def forward_neuralnet(x):
    global weight, bias
    output = np.matmul(x, weight) + bias # 신경망 출력 -> 가중치 곱셈은 행렬끼리 곱셈, 편향 덧셈은 행렬과 벡터의 덧셈
    return output

def backprop_neuralnet(G_output, x):
    global weight, bias
    g_output_w = x.transpose()

    G_w = np.matmul(g_output_w, G_output) # weight, bias의 손실 기울기
    G_b = np.sum(G_output, axis = 0)

    weight -= LEARNING_RATE * G_w
    bias -= LEARNING_RATE * G_b

def run_train(x, y): # 미니배치 학습 처리 담당
    output, aux_nn = forward_neuralnet(x) # 순전파 처리
    loss, aux_pp = forward_postproc(output, y) # 손실함수 loss 계산
    accuracy = eval_accuracy(output, y) # 보고용 정확도 계산 -> accuracy 변수 저장

    G_loss = 1.0 # 역전파 시작점
    G_output = backprop_postproc(G_loss, aux_pp) # 역전파 처리 / G_output 구하기
    backprop_neuralnet(G_output, aux_nn)
    return loss, accuracy

def run_test(x, y):
    output, _ = forward_neuralnet(x) # 역전파용 보조 정보 무시
    accuracy = eval_accuracy(output, y) # 정확도 계산 후 반환
    return accuracy

def arrange_data(mb_size):
    global data, shuffle_map, test_begin_idx
    shuffle_map = np.arange(data.shape[0]) # 데이터의 수 만큼 일련번호 발생
    np.random.shuffle(shuffle_map) # 셔플
    step_count = int(data.shape[0] * 0.8) // mb_size # 미니배치 처리 스탭 수 반환
    test_begin_idx = step_count * mb_size
    return step_count

def get_test_data():
    global data, shuffle_map, test_begin_idx, output_cnt
    test_data = data[shuffle_map[test_begin_idx:]]
    return test_data[:, :-output_cnt], test_data[:, -output_cnt:]

def get_train_data(mb_size, nth):
    global data, shuffle_map, test_bdgin_idx, output_cnt
    if nth == 0: # 에포크 첫번째 호출 -> 셔플
        np.random.shuffle(shuffle_map[:test_begin_idx])
    train_data = data[shuffle_map[mb_size*nth:mb_size*(nth+1)]]
    return train_data[:, :-output_cnt], train_data[:, -output_cnt:]

def train_and_test(epoch_count, mb_size, report):
    step_count = arrange_data(mb_size)
    test_x, test_y = get_test_data()

    for epoch in range(epoch_count): # 에포크 수 만큼 학습 반복
        losses, accs = [], []

        for n in range(step_count): # step_count 만큼 미니배치 처리 반복
            train_x, train_y = get_train_data(mb_size, n)
            loss, acc = run_train(test_x, test_y)
            losses.append(loss)
            accs.append(acc)

            if report > 0 and (epoch + 1) % report == 0: # 검사
                acc = run_test(test_x, test_y)
                print('Epoch {}: loss = {:5.3f}, acc = {:5.3f}/{:5.3f}'.format(epoch + 1,
                                                                               np.mean(losses),np.mean(accs), acc))

    final_acc = run_test(test_x, test_y)
    print('\nFinal: final acc = {:5.3f}'.format(final_acc))


def abalone_exec(epoch_count = 10, mb_size = 10, report = 1):
    load_abalone_dataset()
    init_model()
    train_and_test(epoch_count, mb_size, report)

abalone_exec()