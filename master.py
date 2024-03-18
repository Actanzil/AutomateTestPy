import openpyxl

workbook = openpyxl.load_workbook("data/electiondata.xlsx")
sheet = workbook['Sheet2']

total_rows = sheet.max_row
total_cols = sheet.max_column

print(total_rows)
print(total_cols)