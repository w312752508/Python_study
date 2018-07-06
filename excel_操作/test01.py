from openpyxl import load_workbook
import xlwings as xw
def inset_record(file_dir,del_record_list):
    wb = load_workbook(file_dir)
    wb_sheet = wb["账号清理记录"]
    if len(del_record_list) == 0:
        print("无删除账号，无删除记录需添加")
    else:
        for i in del_record_list:
           i +=["","离职"]
           wb_sheet.append(i)
           print(i[0],"删除记录添加成功")
        wb.save(file_dir)

file_dir = "d:\\excel_test\\user_list.xlsx"
inset_record(file_dir,del_record_list)


