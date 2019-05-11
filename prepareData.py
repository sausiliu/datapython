import xlwt
import pymysql
from docx import Document


def export_data_word(sqls):
    document = Document()
    document.add_heading(u'我的一个新文档', 0)

    print(document)
    table = document.add_table(rows=2, cols=2)


    ## 执行多个sql查询语句，并写入excel
    #for sql in sqls:
    #    db = pymysql.connect(
    #        host='10.10.30.25',
    #        user='root',
    #        passwd='1',
    #        port=3306,
    #        charset='utf8')

    #    cursor = db.cursor()  # 建立游标
    #    cursor.execute(sql)
    #    data = cursor.fetchall()
    #    fields = cursor.description
    #    # print("len fields: {}".format(len(fields)))
    #    # print("len data: {}".format(len(data)))

    #    db.close()

    # cells = table.add_row().cells
    cell = table.cell(0, 0)
    cell.text = "hello"
    cell = table.cell(0, 1)
    cell.text = "world"
    #print(cell)

    document.save('./test.docx')


def export_data_excel(sqls):

    # Create xlsx
    excel = xlwt.Workbook()
    sheet = excel.add_sheet(u'sheet1', cell_overwrite_ok=True)

    global_c = 0

    # 执行多个sql查询语句，并写入excel
    for sql in sqls:
        db = pymysql.connect(
            host='10.10.30.25',
            user='root',
            passwd='1',
            port=3306,
            charset='utf8')

        cursor = db.cursor()  # 建立游标
        cursor.execute(sql)
        data = cursor.fetchall()
        fields = cursor.description
        # print("len fields: {}".format(len(fields)))
        # print("len data: {}".format(len(data)))

        db.close()
        # 写入行名称
        for i in range(len(fields)):
            print(fields[i][0])
            sheet.write(0, i+global_c, fields[i][0])

        # 写内容
        for r in range(len(data)):
            for c in range(len(fields)):
                #  print(sensor_data[r][c])
                sheet.write(1+r, c+global_c, data[r][c])

        global_c = global_c + len(fields)
    # sensor_data = cursor.fetchone()

    excel.save('test.xls')


def set_style(name, height, bold=False):

    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font

    return style


if __name__ == "__main__":
    # data = xlrd.open_workbook('./data.xlsx')

    # sheet1 = data.sheets()[0]
    # # sheet1 = data.sheet_by_index(0)
    # sheet1 = data.sheet_by_name(u'Sheet1')

    # print(sheet1)
    # print('sheel :\nrow: {} ,col: {}'.format(sheet1.nrows, sheet1.ncols))

    # print(sheet1.col_values(1))
    # # print(sheet1.row_values(0))

    # # Create xlsx
    # excel = xlwt.Workbook('text.xlsx')

    # sheet = excel.add_sheet(u'sheet1', cell_overwrite_ok=True)
    sqls = [
        """SELECT * FROM `performance_schema`.`file_summary_by_event_name` LIMIT 0,1000""",
        """SELECT * FROM `performance_schema`.`file_summary_by_event_name` LIMIT 0,1000""",
        """SELECT * FROM `performance_schema`.`file_summary_by_event_name` LIMIT 0,1000""",
    ]
    #export_data_excel(sqls)
    export_data_word(sqls)

