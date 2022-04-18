import dataset
import math_util
import numpy as np

class AbaloneDataset(dataset.Dataset):
    def __init__(self):
        super(AbaloneDataset, self).__init__('abalone', 'regression')

        rows, _ = math_util.load_csv('D:/python_project/nalcoding/Datasets/abalone.csv')

        xs = np.zeros([len(rows), 10])
        ys = np.zeros([len(rows), 1])

        for n, row in enumerate(rows):
            if row[0] == 'I':
                xs[n, 0] = 1
            if row[0] == 'M':
                xs[n, 1] = 1
            if row[0] == 'F':
                xs[n, 2] = 1
            xs[n, 3:] = row[1:-1]
            ys[n, :] = row[-1:]

        self.dataset.shuffle_data(xs, ys, 0.0)

    def visualize(self, xs, estimates, answers):
        for n in range(len(xs)):
            x, est, ans = xs[n], estimates[n], answers[n]
            xstr = math_util.vector_to_str(x, '%4.2f')
            print('{} => 추정 {:4.1f} : 정답 {:4.1f}'.format(xstr, est[0], ans[0]))
