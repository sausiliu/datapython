import xlwt
import xlrd
import pymysql
import pandas as pd
from docx import Document
# import data_connection_ffm as con

global database=None


def connect_mysql():
    db = pymysql.connect(
         host='10.211.55.5',
         user='root',
         passwd='1',
         port=3306,
         charset='utf8')
    return db


def create_paragraph1(sqls, document):
    # print(sql)

    first = True
    for sql in sqls:
        db = pymysql.connect(
            charset='utf8')

        if first:
            df = pd.read_sql(sql, con=db)
        else:
            df = pd.concat([df, pd.read_sql(sql, con=db)], sort=False)

        db.close()
        first = False

    print(df)

    # Add paragraph
    text = df.at[0, 'count_interest_all'] # 获取特定的值
    document.add_paragraph(u'在这里可以添加文本:' + str(text) +
                           u' :添加文本结束\n')

    print(text)


def create_paragraph2(sqls, document):
    # print(sql)

    first = True
    for sql in sqls:
        db = pymysql.connect(
            host='10.10.8.52',
            charset='utf8')

        if first:
            df = pd.read_sql(sql, con=db)
        else:
            df = pd.concat([df, pd.read_sql(sql, con=db)], sort=False)

        db.close()
        first = False

    print(df)

    # Add paragraph

    text = df.at[0, 'count_interest_28']  # 获取特定的值
    document.add_paragraph(u'在这里可以添加文本2:' + str(text) +
                           u' :添加文本结束\n')

    print(text)


def create_paragraph3(sqls, document):
    # print(sql)

    first = True
    for sql in sqls:
        db = pymysql.connect(
            charset='utf8')

        if first:
            df = pd.read_sql(sql, con=db)
        else:
            df = pd.concat([df, pd.read_sql(sql, con=db)], sort=False)

        db.close()
        first = False

    print(df)

    # Add paragraph
    text = df.at[0, 'count'] # 获取特定的值
    # text = df.at[0, 'count_interest_28']  # 获取特定的值
    document.add_paragraph(u'在这里可以添加文本:' + str(text) +
                           u' :添加文本结束\n')

    text = df.at[0, 'count']  # 获取特定的值
    document.add_paragraph(u'在这里可以添加文本2:' + str(text) +
                           u' :添加文本结束\n')
    print(text)


def create_table(sqls, document):
    # print(sql)

    # 创建word table
    # 读取mysql数据，并且组合放入pandas中
    first = True
    for sql in sqls:
        db = pymysql.connect(
            charset='utf8')

        if first:
            df = pd.read_sql(sql, con=db)
        else:
            df = pd.concat([df, pd.read_sql(sql, con=db)], sort=False)

        db.close()
        first = False

    print(df)

    table = document.add_table(df.shape[0] + 1, df.shape[1], style='Table Grid')

    # Add table
    # add the header rows.
    for j in range(df.shape[-1]):
        table.cell(0, j).text = df.columns[j]

    # add the rest of the data frame
    for i in range(df.shape[0]):
        for j in range(df.shape[-1]):
            table.cell(i + 1, j).text = str(df.values[i, j])

    # 行求和df.iloc[0,0:].sum()


def paste_table_word(path):

    readbook = xlrd.open_workbook(path)
    sheet = readbook.sheet_by_index(0)
    # sheet = readbook.sheet_by_name()

    ncols = sheet.ncols
    nrows = sheet.nrows
    print("create a table {} x {} ".format(ncols, nrows))

    document = Document()
    # document.add_heading(u'我的一个新文档', 0)

    # export_data_word(sqls)
    document.add_paragraph("This style is : ")
    table = document.add_table(rows=nrows, cols=ncols, style='Table Grid')

    for r in range(nrows):
        for c in range(ncols):
            #print(sheet.cell(r, c))
            cell = table.cell(r, c)
            cell.text = u'' + str(sheet.cell(r, c).value)

    # table.add_row()
    table.add_column(10)

    document.save('./test.docx')


def export_data_excel(sqls, excel):

    sheet = excel.add_sheet(u'sheet1', cell_overwrite_ok=True)

    global_c = 0

    # 执行多个sql查询语句，并写入excel
    for sql in sqls:
        db = pymysql.connect(
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
            # print(fields[i][0])
            sheet.write(0, i+global_c, fields[i][0])

        # 写内容
        for r in range(len(data)):
            for c in range(len(fields)):
                #  print(sensor_data[r][c])
                sheet.write(1+r, c+global_c, data[r][c])

        global_c = global_c + len(fields)
    # sensor_data = cursor.fetchone()


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

    # 1. 链接数据库
    database = connect_mysql()

    sqls = [
        """select month(MEASURE_DATETIME)as month,count(*) as count_interest_all from SENSOR1.T_GRID_OF_INTEREST 
        where MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31' 
        and REASON not like '' and DELETE_FLAG=0 group by year(MEASURE_DATETIME),month(MEASURE_DATETIME)""",
        """select month(MEASURE_DATETIME)as month,count(*) as count_interest_28 from SENSOR1.T_GRID_OF_INTEREST 
        where MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31' and REASON not like '' and DELETE_FLAG=0 
        and CITY_ID in (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_28') 
        group by month(MEASURE_DATETIME)""",
        """select CITY_NAME, COUNT(CITY_NAME) AS interest_reason from SENSOR1.T_GRID_OF_INTEREST 
        where MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31' 
        and REASON not like '' AND REASON LIKE '%且%'and DELETE_FLAG=0 
        and CITY_ID in (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_28') 
        group by CITY_NAME"""
    ]

    # export_data_excel(sqls)

    # paste_table_word('./test.xls')

    # Create word
    document = Document()

    # create_table(sqls, document)
    sql1 = ["""select month(MEASURE_DATETIME)as month,count(*) as count_interest_all from SENSOR1.T_GRID_OF_INTEREST 
        where MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31' 
        and REASON not like '' and DELETE_FLAG=0 group by year(MEASURE_DATETIME),month(MEASURE_DATETIME)"""]
    sql2 = ["""select month(MEASURE_DATETIME)as month,count(*) as count_interest_28 from SENSOR1.T_GRID_OF_INTEREST 
        where MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31' and REASON not like '' and DELETE_FLAG=0 
        and CITY_ID in (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_28') 
        group by month(MEASURE_DATETIME)"""]

    create_paragraph1(sql1, document)
    create_paragraph2(sql2, document)

    document.save('test.docx')

    # ----------------------
    # time.sleep(1)
    # Create xlsx
    #excel = xlwt.Workbook()
    #export_data_excel(sqls, excel)
    #excel.save('test.xls')

    # end: 关闭数据库
    database.close()