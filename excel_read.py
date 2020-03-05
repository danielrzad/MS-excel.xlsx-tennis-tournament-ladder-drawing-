from openpyxl import load_workbook


wb = load_workbook(filename="sample.xlsx")
# if not wb.views:
#     wb.views.append(openpyxl.workbook.views.BookView())
print(wb.sheetnames)