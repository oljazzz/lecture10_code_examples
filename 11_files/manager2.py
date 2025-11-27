from multiprocessing import Process, Manager


def inc(shared):
    shared['count'] += 1


if __name__ == '__main__':
    with Manager() as manager:
        shared = manager.dict(count=0)
        procs = [Process(target=inc, args=(shared,)) for _ in range(5)]
        for p in procs: p.start()
        for p in procs: p.join()
        print(shared['count'])  # 5
