import multiprocessing


def find_cubes(newlist, data, val):
    for idx, n in enumerate(newlist):
        data[idx] = n ** 3
    val.value = sum(data)
    print("Data in process is ", data[:])
    print("Value in process is ", val.value)


if __name__ == '__main__':
    data = multiprocessing.Array('i', 3)
    val = multiprocessing.Value('i')
    newlist = [3, 4, 5]
    p5 = multiprocessing.Process(target=find_cubes, args=(newlist, data, val))
    p5.start()
    p5.join()
    print("Main program value is ", val.value)
    print("Main program data is ", data[:])
