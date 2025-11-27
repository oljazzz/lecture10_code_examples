import multiprocessing
import time

def heavy_calculation(n):
    """Тяжелое вычисление - считаем сумму квадратов"""
    result = sum(i * i for i in range(n))
    return result

def main():
    numbers = [5000000, 5000000, 5000000, 5000000]

    # Последовательно
    start = time.time()
    results = [heavy_calculation(n) for n in numbers]
    print(f"Последовательно: {time.time() - start:.2f} сек")

    # Параллельно
    start = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(heavy_calculation, numbers)
    print(f"Параллельно: {time.time() - start:.2f} сек")


if __name__ == "__main__":
    multiprocessing.freeze_support()   # Windows requirement
    main()
