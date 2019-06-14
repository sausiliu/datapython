from windrose import WindroseAxes
import pandas as pd
import numpy as np

# 读取第一列
data = pd.read_csv('./wind.csv', usecols=[0])
# 行列矩阵转换一下
#data_values = data.values
#print(type(data_values))
#print(np.transpose(data_values)[0])

data = pd.read_excel('./wind.xlsx', sheet_name='wind')
data_values = data.values
print(np.transpose(data_values)[0])

# 使用nmupy随机生成风速风向数组
# ws = np.random.random(500) * 6
# wd = np.random.random(500) * 360

# print(type(ws))
# print(ws)
# 绘图
# ax = WindroseAxes.from_ax()
# ax.bar(wd, ws, normed=True, opening=0.8, edgecolor='white')
# ax.set_legend()
