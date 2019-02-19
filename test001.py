import threading
import requests

str = ''

def find1():
    lock.acquire()
    global str
    res =requests.get(url='http://mirrors.163.com/centos/6/isos/x86_64/README.txt')
    str = str + res.text

    lock.release()

def find2():
    global str
    lock.acquire()
    res =requests.get(url='http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt')
    str = str + res.text

    lock.release()

def write():
    global str
    lock.acquire()
    fp = open('readme89.TXT ','w')
    fp.write(str)
    fp.close()
    lock.release()


if __name__ == '__main__':
    lock = threading.Condition()
    t1 = threading.Thread(target=find1)
    t2 = threading.Thread(target=find2)
    t3 = threading.Thread(target=write)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()