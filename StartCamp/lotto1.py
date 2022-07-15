import requests
import random
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1023'
response = requests.get(url).json()
lotto_number = [response['drwtNo1'],response['drwtNo2'],response['drwtNo3'],response['drwtNo4'],response['drwtNo5'],response['drwtNo6']]
bonus_number = response['bnusNo']
print(f'당첨번호 : {lotto_number}')
print(f'보너스 번호 : {bonus_number}')

first, second, third, forth, fifth, fail, tries, money = 0, 0, 0, 0, 0, 0, 0, 0
howmany = int(input('시도해볼 시뮬레이션 횟수: '))

while tries < howmany:
    my_number = random.sample(range(1,46),6)
    result = 0
        
    for i in my_number:
        if i in lotto_number:
            result += 1   
    
    if result == 6:
        first += 1
        money += 2745677875
    elif result == 5 and bonus_number in my_number:
        second += 1
        money += 57201623
    elif result == 5 and not bonus_number in my_number:
        third += 1
        money += 1643463
    elif result == 4:
        forth += 1
        money += 50000
    elif result == 3:
        fifth += 1
        money += 5000
    else:
        fail += 1
        money -= 1000
    
    tries += 1


print(f'결과: [1등: {first}회, 2등: {second}회, 3등: {third}회, 4등: {forth}회, 5등: {fifth}회, 꽝: {fail}회]')
print(f'총 횟수: {tries}회, 손익: {money:,}원')