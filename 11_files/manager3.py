from multiprocessing import Manager, Process


def add_data(shared_list):
    shared_list.append("Data")

if __name__ == "__main__":
    manager = Manager()
    shared_list = manager.list()
    p1 = Process(target=add_data, args=(shared_list,))
    p2 = Process(target=add_data, args=(shared_list,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(shared_list)