# 오전과 오후를 구분 하는 프로그램

# 날짜/시간과 관련된 기능을 가져옵니다.
import datetime

# 현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

# 오전 구분
if now.hour < 12:
   print("현재 시각은 {}시로 오전 입니다".format(now.hour))
   
# 오후 구분
if now.hour >= 12:
   print("현재 시각은 {}시로 오후 입니다!.".format(now.hour))