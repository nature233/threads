import queue
import threading
import random
import time
class Producer(threading.Thread):
    """docstring for Producer"""
    def __init__(self, q, name):
        super(Producer, self).__init__()
        self.q = q
        self.name = name
        print ('prodocer %s start' % self.name)
    def run(self):
        for i in range(0, 100):
            resource = random.randint(1, 100)
            try:
                self.q.put(resource, block=True, timeout=3)
            except queue.Full:
                print ('queue is full, %s will exit' % self.name)
            print ('%s: res %i in queue' % (self.name, resource))
class Consumer(threading.Thread):
    """docstring for Consumer"""
    def __init__(self, q, name):
        super(Consumer, self).__init__()
        self.q = q
        self.name = name
        print ('consumer %s start' % name)
    def run(self):
        for i in range(0, 100):
            try:
                res = self.q.get(block=True, timeout=3)
                self.q.task_done()
            except queue.Empty:
                print ('queue is empty, %s will exit' % self.name)
                break
            else:
                print ('%s:res %s out queue' % (self.name, str(res)))
queue = queue.Queue(40)
for i in range(0, 5):
    p = Producer(queue, 'p%i' % i)
    p.start()
for i in range(0,10):
    c = Consumer(queue, 'c%i' % i)
    c.start()