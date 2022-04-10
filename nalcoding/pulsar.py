import csv
import numpy as np

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