import openpyxl

path = "C:\Pranay\PythonWorkspace\Python_Automation\Test1.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active

for r in range(1, 5):  # it will take 4 rows
    for c in range(1, 4):  # it will take 3 columns
        sheet.cell(row=r, column=c).value = "Welcome"

workbook.save(path)