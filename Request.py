import requests

response = requests.get(url = "https://jsonplaceholder.typicode.com/posts", params="")
print(response.json())