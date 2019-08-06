from multiprocessing import Process
from multiprocessing import Queue
from time import sleep

counter = 0


def sub_task(q, string):
    # global counter
    # while counter < 10:
    #     print(string, end='', flush=True)
    #     counter += 1
    #     sleep(0.01)
    try:
        while True:
            num = q.get(block= False)
            if num >= 10:
                break
            else:
                print(string, end = ' ', flush=True)
                q.put(num+1, block=False)
                sleep(0.01)

    except:
        pass


def main():
    q = Queue()
    q.put(0, block = False)
    Process(target=sub_task, args=(q, 'Ping',)).start()
    Process(target=sub_task, args=(q, 'Pong',)).start()


if __name__ == '__main__':
    main()