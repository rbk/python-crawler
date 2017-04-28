import requests

r = requests.get('https://cliniciansbrief.com', timeout=5)
print(r.url)
print(r.text)