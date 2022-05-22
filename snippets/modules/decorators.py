import time


def timer_decorator(func):
    """timer decorator for debug"""
    def f(*args, **kwargs):
        before = time.time()
        val = func(*args, **kwargs)
        after = time.time()
        print("[*] elapsed time: {}[s] ({})".format(after-before, func.__name__))
        return val
    return f
    
    
if __name__ == "__main__":
    pass
    
    