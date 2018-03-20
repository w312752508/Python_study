from openpyxl import load_workbook

wb= load_workbook("d:\\excel_test\\user_list.xlsx")
wb_sheet1 =wb["堡垒机"]
wb_sheet2 =wb["跳板机"]
with open("001.txt","r") as fs :
    for i in fs :
        i_list = i.split(",")
        for r in wb_sheet1.rows:
            for ce in r :
                if str(i_list[0].strip()) == str(ce.value) :
                    wb_sheet1.cell(row=ce.row, column=9).value = i_list[1]
                    wb_sheet1.cell(row=ce.row, column=10).value = i_list[2]
                    wb_sheet1.cell(row=ce.row, column=11).value = i_list[3]
        for r2 in wb_sheet2.rows:
            for ce2 in r2:
                if str(i_list[0].strip()) == str(ce2.value):
                    print(wb_sheet2.cell(row=ce2.row, column=1).value,i_list[0].strip(),
                          wb_sheet2.cell(row=ce2.row, column=6).value)
                    wb_sheet2.cell(row=ce2.row, column=9).value = i_list[1]
                    wb_sheet2.cell(row=ce2.row, column=10).value = i_list[2]
                    wb_sheet2.cell(row=ce2.row, column=11).value = i_list[3]

wb.save("d:\\excel_test\\user_list_new.xlsx")