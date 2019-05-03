import xlwt
import xlrd


def set_style(name, height, bold=False):
    style = xlwt.XFStyle() #初始化样式

    font = xlwt.Font()
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.colour_index = 4
    font.height = height

    style.font = font

    return style


if __name__ == "__main__":
    data = xlrd.open_workbook('./data.xlsx')

    sheet1 = data.sheets()[0]
    # sheet1 = data.sheet_by_index(0)
    sheet1 = data.sheet_by_name(u'Sheet1')

    print(sheet1)
    print('sheel :\nrow: {} ,col: {}'.format(sheet1.nrows, sheet1.ncols))

    print(sheet1.col_values(1))
    # print(sheet1.row_values(0))

    # Create xlsx
    excel = xlwt.Workbook('text.xlsx')

    sheet = excel.add_sheet(u'sheet1', cell_overwrite_ok=True)

