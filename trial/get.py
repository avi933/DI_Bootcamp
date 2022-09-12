import requests
url = 'https://codeforgeek.com'
data = {'key': 'value'}

r = requests.post(url, data = data)

print(r.text) 