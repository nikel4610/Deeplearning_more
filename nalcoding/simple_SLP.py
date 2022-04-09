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

def abaloine_exec(epoch_count = 10, mb_size = 10, report = 1):
    load_abalone_dataset()
    init_model()
    train_and_test(epoch_count, mb_size, report)