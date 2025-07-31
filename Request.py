import requests

# 1
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}
response = requests.get("https://jsonplaceholder.typicode.com/posts", headers=headers)
if response.status_code == 200:
    data = response.json()
    print(f"Username: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
else:
    print("Failed to retrieve data.")


# 2 Post Call
payload = {
    "name": "Suraj",
    "email": "suraj@example.com"
}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.json())


# 3 Downalod File
url = "https://www.example.com/sample.pdf"
response = requests.get(url)

with open("sample.pdf", "wb") as f:
    f.write(response.content)
print("Download complete.")


