#Index error
format_a = "{}만 원\n".format(5000)
format_b = "파이썬 빡공하여 첫 연봉{}만 원 만들기\n".format(5000)
format_c = "{}{}{}{}\n".format(3000,5000,10000)
# IndexError: Replacement index 3 out of range for positional args tuple
format_d = "{}{}{}{}\n".format(1,"문자열",True)
# IndexError: Replacement index 3 out of range for positional args tuple

# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)
