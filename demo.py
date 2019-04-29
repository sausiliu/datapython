# coding=utf-8

# filename可以直接从盘符开始，标明每一级的文件夹直到csv文件，

import pandas as pd
import numpy as np

# import csv

data = pd.read_csv('./sales-funnel.csv', index_col=0)

print('head:')
print(data.head())
print('\n\ntail:')
print(data.tail())

print('\n\n------------:')

table = pd.pivot_table(data,index=["Manager","Rep"],values=["Price"],aggfunc=np.sum)
print(table)
# table.to_csv('test.csv', encoding='utf_8_sig')

