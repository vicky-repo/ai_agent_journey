import requests
api_url = "https://jsonplaceholder.typicode.com/posts/5"
response = requests.get(api_url)
data = response.json()
print(data)
print(f"Title: {data['title']}")
print(f"Body: {data['body']}")
