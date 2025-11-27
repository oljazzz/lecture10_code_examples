import multiprocessing


def sender(conn, messages):
    for message in messages:
        conn.send(message)
        print("Send this: ", message)
    conn.close()

def receiver(conn):
    while 1:
        message = conn.recv()
        if message == "END":
            break
        print("Received this: ", message)

if __name__ == '__main__':
    messages = ["hello", "can you hear me?", "I'm in Amsterdam",
                "Waiting", "Thinking about how we used to be"]
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, messages))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()