from multiprocessing import Pool, freeze_support
from PIL import Image
import os
import time


def resize_image(filename):
    """Resize image and save into C:/tmp/resized directory."""
    output_dir = "C:/tmp/resized"
    os.makedirs(output_dir, exist_ok=True)

    img = Image.open(filename)
    img.thumbnail((800, 800))

    base = os.path.basename(filename)
    save_path = os.path.join(output_dir, base)

    img.save(save_path)
    return save_path


if __name__ == "__main__":
    freeze_support()  # Windows-та multiprocessing дұрыс жұмыс істеуі үшін

    images = [
        "C:/tmp/image1.jpg",
        "C:/tmp/image2.jpg",
        "C:/tmp/image3.jpg",
        "C:/tmp/image4.jpg"
    ]

    # Sequential processing
    start = time.time()
    for img in images:
        resize_image(img)
    print(f"Последовательно: {time.time() - start:.2f} сек")

    # Parallel processing
    start = time.time()
    with Pool(processes=4) as pool:
        results = pool.map(resize_image, images)
    print(f"Параллельно: {time.time() - start:.2f} сек")

    print("Готово! Файлы сохранены в C:/tmp/resized")
