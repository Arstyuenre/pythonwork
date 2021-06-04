import time
import functools


def dec(text=''):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            t_begin = time.time()
            print('%s 开始于 %0.4f' % (fn.__name__, t_begin))
            res = fn(*args, **kwargs)
            t_end = time.time()
            print('%s 结束于 %0.4f' % (fn.__name__, t_end))
            print('%s%s 于 %s ms 内执行完毕' % (text, fn.__name__, t_end - t_begin))
            return res

        return wrapper

    return metric


@dec()
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@dec()
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(10, 20)
s = slow(10, 20, 30)
if f != 30:
    print('测试失败!')
elif s != 6000:
    print('测试失败!')
