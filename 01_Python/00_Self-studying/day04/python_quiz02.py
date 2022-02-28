str_input = input("원의 반지름 입력 >")
num_input = float(str_input)
print()
print("반지름: ",num_input)
# print("둘레 ", 2 * 3.14 * str_input)
# print("넓이 ", 3.14 * str_input ** 2)
print("둘레 ", 2 * 3.14 * num_input)
print("넓이 ", 3.14 * num_input ** 2)

# print("둘레 ", 2 * 3.14 * num_input),print("넓이 ", 3.14 * num_input ** 2)
# 앞에서 이 소스코드가 정상적으로 출력이 되었던 이유는 input 함수가 str_input의 변수에 할당이 되고 intput 함수에 입력된 숫자는 str_input에 저장이 되고 num_input = float(str_input) 문자열에서 실수타입(부동소수점)으로 변환 할 때 str_input에 담겨진 임의의 숫자를 호출 하여 num_input에 저장해서 print() 출력 함수로 값이 나오는게 정상적인 루트이지만 어차피 str_input에 입력된 임의의 값을 참조 해서 한 것이니 값을 출력 할 때는 아무 이상은 없지만 협업 할 때는 서로 코드가 동일 해야 하니, 이 점 반드시 지키며 하자.   