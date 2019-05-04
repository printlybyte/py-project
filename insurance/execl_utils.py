import xlwt
import xlrd


class excel_write_C():
    def __init__(self):
        pass



    # 写入excel,注意保存文件格式
    def write_m(self,sheet_name,filename,rows,lines,content):
        # 创建workbook（其实就是excel，后来保存一下就行）
        workbook = xlwt.Workbook(encoding='ascii')
        # 创建表
        worksheet = workbook.add_sheet(sheet_name)
        # 往单元格内写入内容
        worksheet.write(rows, lines, label=content)
        # 保存
        workbook.save(filename)


if __name__ == "__main__":
    mExeclUtils = excel_write_C()
    mExeclUtils.write_m('My Worksheet','Excel_Workbook.xls')
