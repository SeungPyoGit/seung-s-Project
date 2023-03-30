import openpyxl as excel

#새로운 워크북 생성
book = excel.Workbook()

#엑셀 시트 활성화하고, 시트의 셀 A1의 작성

sheet = book.active
sheet["A1"] = "헬로우 파이썬 엑셀"

book.save("py_excel01.xlsx")