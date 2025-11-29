from multiprocessing import Value, Process


def increment(number):
    number.value += 10


if __name__ == "__main__":
    num = Value('i', 0)
    p1 = Process(target=increment, args=(num,))
    p2 = Process(target=increment, args=(num,))
    p3 = Process(target=increment, args=(num,))


    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()

    print("Main program value is ", num.value)
