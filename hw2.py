import datetime

number = int( input('차량번호 입력 : ') )

day = datetime.datetime.now().day
str1 = ''

if day%2 == 0:
    str1 = '짝수날'
else:
    str1 = '홀수날'

if (day%2 == 0 and number%2 == 0) or (day%2 == 1 and number%2 == 1):
    print('오늘은 %d로 %s로 주차가능합니다.' %(day, str1))
else:
    print('오늘은 %d로 %s로 주차 불가능합니다.' %(day, str1))
