import pymysql
import time

if __name__ == "__main__":
    print('main')

    sqls = [
            """SELECT * FROM `performance_schema`.`hosts` LIMIT 0, 1000""",
            """SELECT * FROM `performance_schema`.`hosts` LIMIT 0, 1000""",
            """SELECT * FROM `performance_schema`.`hosts` LIMIT 0, 1000"""
           ]

    db=pymysql.connect(
        host='10.211.55.5',
        user='root',
        passwd='1',
        port=3306,
        charset='utf8')

    cursor = db.cursor()

    for s in sqls:
        print(s)

        cursor.execute(sqls[1])
        data = cursor.fetchall()
        fields = cursor.description
        print(fields)

        for i in range(len(fields)):
            print(fields[i][0])

        for r in range(len(data)):
            for c in range(len(fields)):
                print(data[r][c])
        print('------------------------------')

    db.close()
