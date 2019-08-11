#多进程demo using Pipe
from multiprocessing import Process
from time import sleep
from multiprocessing import Queue, Pipe

counter = 10


def sub_task(string, conn):

    while True:
        flag = conn.recv()
        if flag >= counter:
            # 要告诉另外一个进程，数量已经够了
            conn.send(flag)
            break
        print(string+' NO:' + str(flag), flush=True)
        sleep(0.01)
        conn.send(flag+1)


def main():
    conn1, conn2 = Pipe()
    conn1.send(0)
    Process(target=sub_task, args=('Ping', conn1)).start()
    Process(target=sub_task, args=('Pong', conn2)).start()


if __name__ == '__main__':
    main()