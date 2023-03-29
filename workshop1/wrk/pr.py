import requests

# Make a GET request to a URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Print the response status code and content
print(response.status_code)
print(response.content)

# Make a POST request to a URL with some data
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Print the response status code and content
print(response.status_code)
print(response.content)

