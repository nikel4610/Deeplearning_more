import simple_SLP
import csv
import numpy as np

def load_steel_dataset():
    with open("D:/python_project/nalcoding/Datasets/faults.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        rows = []
        for row in csvreader:
            rows.append(row)

    global data, input_cnt, output_cnt
    input_cnt, output_cnt = 27, 7
    data = np.asarray(rows, dtype = 'float32')

def steel_exec(epoch_count = 10, mb_size = 10, report = 1):
    load_steel_dataset()
    simple_SLP.init_model()
    simple_SLP.train_and_test(epoch_count, mb_size, report)