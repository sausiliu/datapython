import xlwt
import pymysql

# 创建数据表SQL语句
# sql = """select * from
# (select MEASURE_DATETIME as 1月,STAND_GRIDID,PM25 as 1_pm25 from SENSOR1.T_GRID_STAT_FOR_CITY_MONTHLY where
# STAND_GRIDID in
# (select  STAND_GRIDID from SENSOR1.T_GRID_OF_INTEREST where
# MEASURE_DATETIME>='2019-01-01'
# and MEASURE_DATETIME<='2019-01-31' and REASON not like '' and DELETE_FLAG=0
# and CITY_ID in
# (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_11'))
# and MEASURE_DATETIME>='2019-01-01' and MEASURE_DATETIME<='2019-01-31'
# and VAR_TYPE_ID=1 and REGION_LEVEL=0)a
# left join
# (select MEASURE_DATETIME as 2月,STAND_GRIDID,PM25 as 2_pm25 from SENSOR1.T_GRID_STAT_FOR_CITY_MONTHLY where
# STAND_GRIDID in
# (select  STAND_GRIDID from SENSOR1.T_GRID_OF_INTEREST where
# MEASURE_DATETIME>='2019-01-01'
# and MEASURE_DATETIME<='2019-01-31' and REASON not like '' and DELETE_FLAG=0
# and CITY_ID in
# (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_11'))
# and MEASURE_DATETIME>='2019-02-01' and MEASURE_DATETIME<='2019-02-28'
# and VAR_TYPE_ID=1 and REGION_LEVEL=0)b
# on a.STAND_GRIDID=b.STAND_GRIDID
# left join
# (select MEASURE_DATETIME as 3月,STAND_GRIDID,PM25 as 3_pm25 from SENSOR1.T_GRID_STAT_FOR_CITY_MONTHLY where
# STAND_GRIDID in
# (select  STAND_GRIDID from SENSOR1.T_GRID_OF_INTEREST where
# MEASURE_DATETIME>='2019-01-01'and MEASURE_DATETIME<='2019-01-31'
# and REASON not like '' and DELETE_FLAG=0 and CITY_ID in
# (select CITY_ID from SENSOR1.T_DICT_CITY_GROUP where GROUP_ID='HOTGRID_11'))
# and MEASURE_DATETIME>='2019-03-01' and MEASURE_DATETIME<='2019-03-31'
# and VAR_TYPE_ID=1 and REGION_LEVEL=0 )c
# on a.STAND_GRIDID=c.STAND_GRIDID"""

host = '10.112.115.35'
user = 'root',
passwd = '1',
port = 3306,


def export_data(sqls):

    # Create xlsx
    excel = xlwt.Workbook()
    sheet = excel.add_sheet(u'sheet1', cell_overwrite_ok=True)

    global_c = 0

    # 执行多个sql查询语句，并写入excel
    for sql in sqls:
        db = pymysql.connect(
            host='10.112.115.35',
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

        # 写入行名称
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
    export_data(sqls)

