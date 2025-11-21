import asyncio
import aiohttp  # Асинхронная библиотека для HTTP


async def download_page(url):
    """async def - асинхронная функция"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()  # await - ждем результата
            return len(content)


async def main():
    urls = [
        "https://python.org",
        "https://github.com",
        "https://stackoverflow.com"
    ]

    # asyncio.gather - запускаем все задачи одновременно
    results = await asyncio.gather(*[download_page(url) for url in urls])
    print(f"Размеры страниц: {results}")


# Запуск асинхронного кода
asyncio.run(main())