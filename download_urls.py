import threading
import time
import requests  # requests қосу

urls = [
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com"
]

def download(url):
    response = requests.get(url)
    print(f"Загружено: {url} ({len(response.text)} байт)")

start = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Время: {time.time() - start:.2f} сек")
