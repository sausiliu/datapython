# coding=utf-8

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，

import pandas as pd
import numpy as np

# import csv

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，
# header=None表示头部为空，sep=' '表示数据间使用空格作为分隔符
# 如果分隔符是逗号，只需换成 ‘，’即可。
# df=pd.read_csv('filename',header=None,sep=' ')
# ---------------------

data = pd.read_csv('./database.csv', index_col=0)
# data = pd.read_csv('./sales-funnel.csv', index_col=0)
# data = pd.read_csv('./test_database.csv', index_col=0)
# data = pd.read_csv('./data.csv', index_col=0)

# data.sort_values(['Year', "Happiness Score"], ascending=[True, False], inplace=True)

#print('head:')
#print(data.head())
#print('\n\ntail:')
#print(data.tail())

# table = data.pivot_table(data, index=["Country", "Family"])
# table = data.pivot_table(data, index=["区县"], values=["发现问题数"])
# table = data.pivot_table(data, colums=["区县"], values=["发现问题数"])
# table = data.pivot_table(data, columns=["区县"], index=["发现问题数"], aggfunc=np.sum)
# table = data.pivot_table(data, index=["区县"], aggfunc=np.sum)

table = data.pivot_table(data, index=["区县"], values=["Price"], aggfunc=np.sum)
# print(table.ix['范县'])

print(table)
print('\n\n------------:')
#print(table)
# table.to_csv('test.csv', encoding='utf_8_sig')

