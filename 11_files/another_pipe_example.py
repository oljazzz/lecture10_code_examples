import multiprocessing
from multiprocessing import Process


def child(conn):
    conn.send("Hello from child!")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()

    print(parent_conn.recv())
    p.join()
