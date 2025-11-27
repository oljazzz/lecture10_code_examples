import asyncio
import aiohttp
import time

urls = [
    "https://python.org",
    "https://github.com",
    "https://stackoverflow.com"
]

async def download(url, session):
    async with session.get(url) as response:
        text = await response.text()
        print(f"Async: Загружено {url} ({len(text)} байт)")
        return text

async def main():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(*[download(url, session) for url in urls])

if __name__ == "__main__":
    start = time.time()
    results = asyncio.run(main())
    print(f"AsyncIO время: {time.time() - start:.2f} сек")
