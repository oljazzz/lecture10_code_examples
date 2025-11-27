from multiprocessing import Process, Queue


def worker(q):
    q.put('hello1')


if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()
