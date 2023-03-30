menu = {"짜장면":5000, "짬뽕" :6000, "탕수육" : 12000}

menu_sum = 0
answer = "예"

while answer == "예" :
    input_menu = input("메뉴를 선택하세요")
    menu_sum = menu_sum + menu[input_menu]
    answer = input("추가 주문을 하시겠습니까?")

print("결재 금액은", menu_sum, "원 입니다.")