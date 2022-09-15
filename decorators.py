from functools import wraps
from time import sleep, perf_counter_ns


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        func(*args, **kwargs)
        return perf_counter_ns() - start_time
    return wrapper


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        output = func(*args, **kwargs)
        print(output)
        return output
    return wrapper


def delay(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(1)
        return func(*args, **kwargs)
    return wrapper


def questionify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return str(func(*args, **kwargs)) + "?"
    return wrapper


def has_input(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args:
            return func(*args, **kwargs)
        else:
            raise RuntimeError("This function needs arguments")
    return wrapper
