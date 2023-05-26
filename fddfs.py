import requests
url ='http://127.0.0.1:8000/jang/auth'

response = requests.post(url, data={'username': 'admin', 'password': '1541'})

print(response.text)

myToken = response.json()
print(myToken['token'])
token = myToken['token']

header = {'Authorization' : 'Token' + token}
response = requests.get('http://127.0.0.1:8000/jang/', headers=header)
print(response.text)