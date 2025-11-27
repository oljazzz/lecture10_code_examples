import multiprocessing


def find_num(new_list, data, val):
    for idx, num in enumerate(new_list):
        data[idx] = num + 3
    val.value = sum(data)
    print("Data in process 5 is ", data[:])

def subtract_val(new_list, data, val):
    for idx, num in enumerate(new_list):
        data[idx] = num - 3
    print("Data in process 6 is ", data[:])

if __name__ == "__main__":
    data = multiprocessing.Array('i', 3)
    val = multiprocessing.Value('i')
    newlist = [3, 4, 5]
    p5 = multiprocessing.Process(target=find_num, args=(newlist, data, val))
    p6 = multiprocessing.Process(target=subtract_val, args=(newlist, data, val))
    p5.start()
    p6.start()
    p5.join()
    p6.join()
    print("Main program value is ", val.value)
    print("Main program data is ", data[:])