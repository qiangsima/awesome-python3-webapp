# coroutine.py

__author__ = 'sima'

'''
协程方式实现生产者和消费者
'''


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def producer(c):
    c.send(None) # send参数是上一次被挂起的yield语句的返回值
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return %s.' % r)
    c.close()


c = consumer()
producer(c)
