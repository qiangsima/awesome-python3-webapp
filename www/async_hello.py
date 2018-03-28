# async_hello.py

__author__ = 'sima'

'''
asyncio编程模型就是一个消息循环。
从async中获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行
'''

import asyncio
import threading

@asyncio.coroutine
def hello():
    print('Hello World! (%s)' % threading.current_thread())
    r = yield from asyncio.sleep(1)
    print('hello again. (%s)' % threading.current_thread())


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()