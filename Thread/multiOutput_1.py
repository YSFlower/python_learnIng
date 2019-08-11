#多进程demo using Queue
from multiprocessing import Process
from time import sleep
from multiprocessing import Queue
counter = 0

def sub_task(string, q):
    while True:
        if q.empty():
            break
        print(string+' NO:' + str(q.get()), flush=True)
        sleep(0.01)


def main():
    counter = 10
    q = Queue(counter)
    for _ in range(counter):
        q.put(_)
    Process(target=sub_task, args=('Ping', q)).start()
    Process(target=sub_task, args=('Pong', q)).start()


if __name__ == '__main__':
    main()