import threading
import time

import requests


def download(url):
    response = requests.get(url)
    print(f"Загружено: {url}")


start = time.time()
threads = []

urls = [
    "https://api.github.com/users/python",
    "https://api.github.com/users/google",
    "https://api.github.com/users/microsoft"
]

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Время: {time.time() - start:.2f} сек")
