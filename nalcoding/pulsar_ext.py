import pulsar
import simple_SLP
import csv
import numpy as np

def load_pulsar_dataset(adjust_ratio):
    pulsars, stars = [], []
    with open("D:/python_project/nalcoding/Datasets/pulsar_data_test.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        rows = []
        for row in csvreader:
            if row[0] == '1' : pulsars.append(row) # pulsars와 stars를 구분
            else: stars.append(row)
    global data, input_cnt, output_cnt
    input_cnt, output_cnt = 8, 1

    star_cnt, pulsar_cnt = len(stars), len(pulsars)

    if adjust_ratio: # adjust_ratio = True
        data = np.zeros([2*star_cnt, 9])
        data[0:star_cnt, :] = np.array(stars, dtype='float32') # 별 데이터를 data 버퍼에 담은 후
        for n in range(star_cnt): # 반복하여 별 데이터와 펄서 데이터가 같은 수가 되게 만듬
            data[star_cnt*n] = np.asarray(pulsars[n % pulsar_cnt], dtype='float32')
    else: # adjust_ratio = False 이면 그냥
        data = np.zeros([star_cnt + pulsar_cnt, 9])
        data[0:star_cnt, :] = np.array(stars, dtype='float32')
        data[star_cnt:, :] = np.array(pulsars, dtype='float32')

def pulsar_exec(epoch_count = 10, mb_size = 10, report = 1, adjust_ratio = False):
    load_pulsar_dataset(adjust_ratio)
    simple_SLP.init_model()
    simple_SLP.train_and_test(epoch_count, mb_size, report)