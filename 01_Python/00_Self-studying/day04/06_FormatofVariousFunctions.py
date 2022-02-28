#float(부동소수점) 자료형 기본 
output_f = "{:f}".format(52.273) 
output_g = "{:+15f}".format(52.273) #15칸 만들기
output_h = "{:+15f}".format(52.273) #15킨에 부호 추가하기
output_i = "{:+015f}".format(52.273) #15칸에 부호 추가하고 0으로 채우기

print("#기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
print("-----------------------------")

#소수점 아래 자릿수 지정하기
print("#소수점 아래 자릿수 지정하기")
output_a = "{:15.3f}".format(52.273) 
output_b = "{:15.2f}".format(52.273) #15칸 만들기
output_c = "{:15.1f}".format(52.273) #15킨에 부호 추가하기
print(output_a)
print(output_b)
print(output_c)
print("-----------------------------")

#의미 없는 소수점 제거하기
output_a = 52.0
output_b = "{:g}".format(output_a)
print(output_a)
print(output_b)