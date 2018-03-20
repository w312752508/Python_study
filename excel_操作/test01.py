from openpyxl import load_workbook
from openpyxl.utils import get_column_letter,column_index_from_string
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter


excel_info = load_workbook("d:\\excel_test\\test.xlsx")
a_sheet = excel_info["002"]
# b = a_sheet['b1'] #获取指定位置的内容
# a = a_sheet['a1']
#print(b.value) #显示指定位置的值
# print(a_sheet.max_row) #获取最大行数
# print(a_sheet.max_column) #获取最大列数
# print(f'({b.column}, {b.row}) is {b.value}')

# for row in a_sheet.rows: #显示整个表格内容
#     for cell in row:
#         print(cell.value)
#
# for row in list(a_sheet.rows)[2]: #显示指定行所有内容
#     print(row.value)
#
# for i in range(1, 4): #指定A1到B3区域的值
#     for j in range(1, 3):
#         print(a_sheet.cell(row=i, column=j).value)

wb = Workbook()
ws = wb.worksheets[0]
ws.title = "新表1"
ws.cell('A1').value = '%s'%("跟随总数")

print(wb.sheetnames)
# wb['Sheet'].title = 'new'
# print(wb.sheetnames)
