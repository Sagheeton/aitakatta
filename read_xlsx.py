from openpyxl import load_workbook

wb = load_workbook(r'resources/file_example_XLSX_50.xlsx')

sheet = wb.active
print(sheet.cell(row=3, column=2).value)