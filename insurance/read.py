# -*- coding: utf-8 -*-
import xlrd
import numpy as np
from collections import Counter
import xlwt
from datetime import date, datetime


def all_np(arr):
    """获取每个元素的出现次数，使用Numpy"""
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        arr_new = arr[mask]
        v = arr_new.size
        result[k] = v
    return result


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'C:\\Users\\lgd\\Desktop\\3月考勤.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('3月考勤')

    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # # 获取整行和整列的值（数组）
    # rows = sheet2.row_values(1) # 获取第四行内容
    cols = sheet2.col_values(65)  # 获取第1列内容
    cols2 = sheet2.col_values(66)  # 获取第1列内容
    # print (rows)

    # 第一种：
    cols.remove("苗馨幻")
    cols2.remove("工时")
    while '' in cols:
        cols.remove('')
    print(cols)
    print(cols2)
    tempD = {}
    tempDs = []
    for kk in range(1, len(cols)):
        tempD[cols[kk]] = cols2[kk]
        tempDs.append(tempD)
        tempD = {}
    print(tempD)
    print(tempDs)

    repeat = []
    repeat = list(set(cols))

    print(repeat)
    kkint = 0
    for repeatvv in range(1, 2):

        for tempDsvv in range(1, len(tempDs)):
            # print(tempDs[tempDsvv])
            tempbeankey=repeat[repeatvv]
            print("tempbeankey"+tempbeankey)
            tempbean=tempDs[tempDsvv]
            print(tempbean)
            # print(tempbean[tempbeankey])

            # print(tempDs[tempDsvv][repeat[repeatvv]])
            # if repeat[repeatvv] == tempDs[tempDsvv]:
            #     print(kkint + 1)
            #     print(repeat[repeatvv]+"出现了 "+str(kkint)+"次")

    #
    # # 获取单元格内容
    # print (sheet2.cell(1,0).value.encode('utf-8'))
    # print (sheet2.cell_value(1,0).encode('utf-8'))
    # print (sheet2.row(1)[0].value.encode('utf-8'))
    #
    # # 获取单元格内容的数据类型
    # print (sheet2.cell(1,0).ctype)


if __name__ == '__main__':
    read_excel()
