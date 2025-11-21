import asyncio
import io
from multiprocessing import Pool, freeze_support

import aiohttp
from PIL import Image

urls = [
    "https://www.python.org/static/img/python-logo.png",
    "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
]


async def download_one(session, url):
    async with session.get(url) as response:
        print(f"Downloaded: {url}")
        return await response.read()  # return bytes


async def download_images(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_one(session, url) for url in urls]
        return await asyncio.gather(*tasks)


def process_image(image_data):
    """CPU-bound: resize image"""
    img = Image.open(io.BytesIO(image_data))
    img.thumbnail((800, 800))
    return img


def main():
    # Скачиваем изображения (I/O-bound) конкурентно
    images = asyncio.run(download_images(urls))

    # Обрабатываем изображения (CPU-bound) параллельно
    with Pool(processes=4) as pool:
        results = pool.map(process_image, images)

    # Сохраняем результаты
    for i, img in enumerate(results):
        img.save(f"resized_image_{i}.png")
    print("Done!")


if __name__ == "__main__":
    freeze_support()  # для Windows
    main()
