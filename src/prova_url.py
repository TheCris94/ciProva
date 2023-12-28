import requests

url = 'https://api.github.com/repos/apache/commons-io/pulls'
response = requests.get(url)
print(response.status_code)