import xlwt
import xlrd

data = xlrd.open_workbook('./data.xlsx')

# sheet1 = data.sheets()[0]
# sheet1 = data.sheet_by_index(0)
sheet1 = data.sheet_by_name(u'Sheet1')

print(sheet1)
print('sheel :\nrow: {} ,col: {}'.format(sheet1.nrows, sheet1.ncols))

print(sheet1.col_values(1))
#print(sheet1.row_values(0))

