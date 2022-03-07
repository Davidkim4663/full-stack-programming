# 나머지 연산자를 활용해서 짝수와 홀수 구분
number = input("정수 입력> ")
number = int(number)

# 짝수 조건
if number % 2 == 0:
  print("짝수 입니다")

# 홀수 조건
if number % 2 != 0:
  print("홀1수 입니다")