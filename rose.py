from windrose import WindroseAxes
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

# data = pd.read_csv('./wind.csv', index_col=0)
# data = pd.read_csv('./wind.csv', usecols=[0])
data = pd.read_csv('./wind.csv')
#data_matrix = data.as_matrix()
data_values = data.values
# data_array = np.array(data)
# print(data_array)
#print(data_values)
print(type(data_values))

print(np.transpose(data_values)[0])

# print(map(list, zip(*data_values))[0])

# 使用nmupy随机生成风速风向数组
# ws = np.random.random(500) * 6
# wd = np.random.random(500) * 360

# print(type(ws))
# print(ws)
# 绘图
# ax = WindroseAxes.from_ax()
# ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
# ax.set_legend()
