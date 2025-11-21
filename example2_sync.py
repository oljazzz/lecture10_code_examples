import requests
import time

urls = [
    "https://api.github.com/users/python",
    "https://api.github.com/users/google",
    "https://api.github.com/users/microsoft"
]

start = time.time()
for url in urls:
    response = requests.get(url)
    print(f"Загружено: {url}")
print(f"Время: {time.time() - start:.2f} сек")

