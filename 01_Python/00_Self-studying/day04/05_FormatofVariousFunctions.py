#조합해보기
output_h = "{:+5d}".format(52)    #기호를 뒤로 밀기: 양수
output_i = "{:+5d}".format(-52)   #기호를 뒤로 밀기: 음수
output_j = "{:=+5d}".format(52)   #기호를 앞으로 밀기: 양수
output_k = "{:=+5d}".format(-52)  #기호를 앞으로 밀기: 음수
output_l = "{:=+05d}".format(52)  # 0으로 채우기 : 양수
output_m = "{:=+05d}".format(-52) # 0으로 채우기 : 음수
output_m = "{:=0+5d}".format(52) # 조합 순서가 중요하며, 순서를 안 지킬시 이상하게 출력된다.

print("#조합하기")
print(output_h)
print(output_i)
print(output_j)
print(output_k)
print(output_l)
print(output_m)