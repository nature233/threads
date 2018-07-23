
import threading
import testClass
class Th(object):
    def __init__(self):
        for i in range(10000):
            th=threading.Thread(target=testClass.A(i,'aaa','男').run,args=())
            print('--------------the name of thread---------------------:',th.getName())
            th.start()
        th.join()
if __name__ == '__main__':
   t=Th()

