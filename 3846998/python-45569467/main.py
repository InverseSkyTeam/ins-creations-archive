import time


def fn(n: int):
    if n == 0:
        return None
    print(n)
    time.sleep(0.001)
    return fn(n - 1)
    
    
def get_res(fn, *args):
    ret = fn(*args)
    while callable(ret):
        ret = ret()
    return ret


def better_fn(n: int):
    if n == 0:
        return None
    print(n)
    time.sleep(0.001)
    return lambda: better_fn(n - 1)


get_res(better_fn, 10000)
