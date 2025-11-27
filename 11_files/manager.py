import multiprocessing


def add_squared_num(x, new_list):
    new_list.append(x ** 2)
    print("New list is ", new_list)


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        data = manager.list([3, 4, 5])
        new_x = 6
        new_x_2 = 7
        p1 = multiprocessing.Process(target=add_squared_num, args=(new_x, data))
        p2 = multiprocessing.Process(target=add_squared_num, args=(new_x_2, data))
        p1.start()
        p2.start()

        p1.join()
        p2.join()
        print(data)
