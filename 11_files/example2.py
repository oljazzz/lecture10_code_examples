import multiprocessing


def find_area_square(x):
    print("Area is ", x * x)


def find_volume_cube(x):
    print("Volume is ", x * x * x)


def find_area_square_2(x):
    global data
    data.append(x * x)
    print("Added ", x * x)


p1 = multiprocessing.Process(target=find_area_square, args=(5,))
p2 = multiprocessing.Process(target=find_volume_cube, args=(5,))

p3 = multiprocessing.Process(target=find_area_square_2, args=(10,))
p4 = multiprocessing.Process(target=find_area_square_2, args=(100,))

if __name__ == '__main__':
    p3.start()
    p4.start()
    p3.join()
    p4.join()
    print(data)
