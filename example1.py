import threading
import time


def make_coffee():
    print("Начинаю варить кофе...")
    time.sleep(3)  # Имитация ожидания
    print("Кофе готов!")


def toast_bread():
    print("Начинаю жарить тосты...")
    time.sleep(2)
    print("Тосты готовы!")


if __name__ == "__main__":
    # Без потоков - последовательно (5 секунд)
    # make_coffee()
    # toast_bread()

    # С потоками - конкурентно (3 секунды)
    thread1 = threading.Thread(target=make_coffee)
    thread2 = threading.Thread(target=toast_bread)

    thread1.start()  # Запускаем первый поток
    thread2.start()  # Запускаем второй поток

    thread1.join()  # Ждем завершения первого
    thread2.join()  # Ждем завершения второго
