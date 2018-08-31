from threading import Thread, Lock
from time import sleep

def func0():
    t = 0
    while True:
        t += 1
        print("func0 t = {}".format(t))
        sleep(5)
    return 0

def func1():
    print("func1")
    test =input("input test")
    print(test)
    return 0

thrs = []
thrs.append(Thread(target= func0, args= ()))
thrs.append(Thread(target= func1, args= ()))

for t in thrs:
    t.start()
# for t in thrs:
#     t.join()