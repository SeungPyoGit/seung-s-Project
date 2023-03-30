import openpyxl as excel

# 기존 엑셀 불러오기
book = excel.load_workbook("py_excel01.xlsx")

#엑셀 시트 첫번째 선택
sheet = book.worksheets[0]

#시트 첫번째 셀 A1 선택하고 출력
cell = sheet["A1"]

print(cell.value)