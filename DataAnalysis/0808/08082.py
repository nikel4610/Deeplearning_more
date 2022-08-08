import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from  matplotlib import font_manager, rc
import matplotlib.colors as mcolors
import math
import seaborn as sns

font_path="C://Windows//Fonts//malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('./kaggle_survey_2020_responses.csv') # ,header = 1)
# print(data.head())

