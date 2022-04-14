import numpy as np
import time
import os
import csv
import copy
import wave
import cv2
import matplotlib.pyplot as plt

from PIL import Image
from IPython.core.display import HTML

def relu(x):
    return np.maximum(0, x)

def relu_derv(y):
    return np.sign(y)

def sigmoid(x):
    return np.exp(-relu(-x)) / (1.0 + np.exp(-np.abs(x)))

def sigmoid_derv(y):
    return y * (1 - y)

def sigmoid_cross_entropy_with_logits(z, x):
    return relu(x) - x * z + np.log(1 + np.exp(-np.abs(x)))

def sigmoid_corss_entropy_with_logits_derv(z, x):
    return - z + sigmoid(x)

def tanh(x):
    return 2 * sigmoid(2 * x) - 1

def tanh_derv(y):
    return (1.0 + y) * (1.0 - y)

def softmax(x):
    max_elem = np.max(x, axis = 1)
    diff = (x.transpose() - max_elem).transpose()
    exp = np.exp(diff)
    sum_exp = np.sum(exp, axis = 1)
    probs = (exp.transpose() / sum_exp).transpose()
    return probs

def softmax_cross_entropy_with_logits(labels, logits):
    probs = softmax(logits)
    return -np.sum(labels * np.log(probs+1.0e-10), axis = 1)

def softmax_cross_entropy_with_logits_derv(labels, logits):
    return softmax(logits) - labels


