import requests
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1000'
response = requests.get(url).json()
print(response)


#1. lotto api로부터 데이터 받아오기

#2. 지난주 당첨 번호 알아내기(1등만)

#3. random module이 가지고 있는 sample이라는 함수를 사용하여 1부터 45중에 무작위 6개를 뽑는다.

#4. 그 번호가 당첨 번호와 일치하는지 확인한다.

# --- 도전과제

#5. 천번 이상 새로운 로또 번호를 생성하여서 매번 당첨이 되었는지 확인해보는 로직 작성

#6. 1등부터 2등을 포함한(보너스번호까지) 4등까지의 각 당첨 횟수 출력하기