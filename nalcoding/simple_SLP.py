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


def abaloine_exec(epoch_count = 10, mb_size = 10, report = 1):
    load_abalone_dataset()
    init_model()
    train_and_test(epoch_count, mb_size, report)