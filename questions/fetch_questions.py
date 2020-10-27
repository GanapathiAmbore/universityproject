import requests
url='http://127.0.0.1:1234/questions/questions/'
response=requests.get(url,auth=('ganapathi','abcd@1234'))
print(response.json())