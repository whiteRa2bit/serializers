import time

from config import LOOPS


def execute_and_profile(fn, *args, loops=LOOPS, **kwargs):
    start_time = time.time()
    for _ in range(loops):
        fn_result = fn(*args, **kwargs)
    execution_time = time.time() - start_time

    return fn_result, execution_time
