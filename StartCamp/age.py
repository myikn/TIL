import requests

url = 'https://api.agify.io/?name=dave'
response = requests.get(url).json()
print(type(response))
name = response['name']
age = response['age']
count = response['count']

print(f'이름이 {name}인 사람의 나이는 {age} 입니다')