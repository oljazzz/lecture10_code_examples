import multiprocessing


def put_in_queue(new_list, q):
    for n in new_list:
        q.put(n)


def print_queue(q):
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue empty")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4]
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=put_in_queue, args=(my_list, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
