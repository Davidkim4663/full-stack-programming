str_input = float((input("숫자입력")))
# str_input = input("숫자입력") --> string에서 input()함수를 받을 때는 datatype (ex : int((input("숫자입력"))) XX 
num_input = float(str_input)

print()
print(num_input,"inch")
print((num_input * 2.54),"cm")