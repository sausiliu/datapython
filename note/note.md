# Notes

记录开发过程的一些问题和心得


## 透视表

最近才真正接触Exxcel透视表的功能，在进行数据处理的时候，利用透视表对数据进行聚合处理非常的高效。所以如果能自动产生根据需求的透视表，那么可以节省很多时间。

在python中使用强大的pandas来实现对数据的透视表处理。在pandas中提供了接口**pivot_table**

## Pandas

可以阅览[pandas官网](http://pandas.pydata.org/)查看更详细的信息(包含[pdf](http://117.128.6.31/cache/pandas.pydata.org/pandas-docs/stable/pandas.pdf?ich_args2=461-27115917036847_a9bbaaf53a84f3a0e6a84f629d176d3f_10001002_9c89612ad4c0f6d49e39518939a83798_061bfaaa0f142965b5714397065536a6))。

### pivot_table

* 在官方对**pivot_table**的介绍

  ```text
  The function pivot_table() can be used to create spreadsheet-style pivot tables. See the cookbook for some
  advanced strategies.
  It takes a number of arguments:
  • data: a DataFrame object.
  • values: a column or a list of columns to aggregate.
  • index: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on the
  pivot table index. If an array is passed, it is being used as the same manner as column values.
  • columns: a column, Grouper, array which has the same length as data, or list of them. Keys to group by on
  the pivot table column. If an array is passed, it is being used as the same manner as column values.
  • aggfunc: function to use for aggregation, defaulting to numpy.mean.
  ```

  ![avatar](imgs/api-pivot_table.png)


## Excel

## 创建excel

[xlwt官方网址](https://xlwt.readthedocs.io/en/latest/index.html)  
使用xlwt来创建一个新的excel文件，整理操作函数感觉比较简单，复杂的应该是在对单元格的业务操作上。所以先来看看主要接口有哪些

* 创建excel  
    file = xlwt.Workbook()

* 添加sheet  
    sheet = file.add_sheet()  

* 添加sheet  
    [官方说明](https://xlwt.readthedocs.io/en/latest/api.html?highlight=write)  
    sheet = write(r, c, label='', style=<xlwt.Style.XFStyle object>)  


### 合并单元格的处理

#### 读取

由于对excel单元格的处理，遇到合并的情况时候，默认只会读取第一个cell的内容，其余的cell会返回空值。那么如何区分这个单元格本身就是空值，还是由于合并后返回的空值呢？

* 获取合并单元格信息

  **formatting_info**  
  
  > xlrd.open_workbook(r'demo.xlsx',formatting_info=True)  
  > sheet = workbook.sheet_by_name('sheet')  
  > sheet.merged_cells  
  
 
  打开文件时，设置formatting_info为True，默认为False。通过**merged_cells**
  
## Word

python 操作word文档，可以使用python-docx包，里面包含了丰富的功能接口

### 创建word文档

创建docx文件必要步骤
```text
from docx import Documen
document = Document()
document.save('./test.docx')
```

### paragraph

> paragraph = document.add_paragraph(u'添加了文本')

### 标题

* 标题

> document.add_heading('Document Title',0)

* 二级标题

> document.add_heading(u'二级标题',1)

* 三级标题

> document.add_heading(u'二级标题',2)


### table

### 样式

#### table

```text
from docx.enum.style import WD_STYLE_TYPE
styles = document.styles
for s in styles:
    if s.type == WD_STYLE_TYPE.TABLE:
        document.add_paragraph("This style is : " + s.name)
        document.add_table(3, 3, style=s)
        document.add_paragraph('\n')
```

通过上面方式可以枚举出所有的样式, 例如下图所示
![avatar](imgs/table-style-1.png)

![avatar](imgs/table-style-2.png)

## REF

[Pandas Pivot Table Explained](https://pbpython.com/pandas-pivot-table-explained.html)

## MySQL

### 配置

在使用mysql时，需要实现局域网内的访问。mysql默认是绑定本地回环ip地址127.0.0.1。所以我们需要更改这个地址。  
**/etc/mysql/mysql.conf.d/mysqld.cnf**

```text
# bind-address          = 127.0.0.1
```

### 查看mysql状态
> service mysql status

### 查看错误日志信息

cat /var/log/mysql/error.log


### MySQL连接池

[参考链接](https://blog.csdn.net/qq_42483967/article/details/81237953)

