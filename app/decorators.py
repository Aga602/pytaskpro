import time


def log_action(func):
    def logs(*args, **kwargs):
        name = func.__name__
        print(f"The function {name} has began")
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"The function {name} copleted in {elapsed:0.8f}s")
        return result

    return logs
