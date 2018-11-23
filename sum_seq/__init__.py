from multiprocessing import cpu_count, Process
from threading import Thread
from time import perf_counter
from statistics import mean, variance

from sum_seq.python.sum_seq import sum_seq as py_sum_seq
from sum_seq.c.sum_seq import sum_seq as c_sum_seq
from sum_seq.cython.sum_seq import sum_seq as cy_sum_seq


FUNCTIONS = {
    "python": py_sum_seq,
    "c": c_sum_seq,
    "cython": cy_sum_seq,
}


def _sequence_exec(n, val, func):
    start = perf_counter()

    for _ in range(n):
        func(val)

    return perf_counter() - start


def _thread_exec(n, val, func):
    start = perf_counter()

    threads = [Thread(target=func, args=(val, )) for _ in range(n)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    return perf_counter() - start


def _process_exec(n, val, func):
    start = perf_counter()

    processes = [Process(target=func, args=(val, )) for _ in range(n)]
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    return perf_counter() - start


def benchmark_sum_seq(n: int = cpu_count(), val: int = 2 * 10 ** 8, iterations: int = 5):
    print(f"Use n: {n}, val: {val}, iterations: {iterations}")
    result = {(tp, var): [] for tp in FUNCTIONS for var in ["sequence", "thread", "process"]}

    # Warm up
    print("Warm up (single run)")
    for tp, func in FUNCTIONS.items():
        print(f"{tp} (sequence)\t{_sequence_exec(n, val, func):.5}")
        print(f"{tp} (thread)\t{_thread_exec(n, val, func):.5}")
        print(f"{tp} (process)\t{_process_exec(n, val, func):.5}")

    # Benchmark
    print("Start benchmark")
    for _ in range(iterations):
        print(f".. {_ + 1}/{iterations}")
        for tp, func in FUNCTIONS.items():
            result[(tp, "sequence")].append(_sequence_exec(n, val, func))
            result[(tp, "thread")].append(_thread_exec(n, val, func))
            result[(tp, "process")].append(_process_exec(n, val, func))

    print("Results\n")
    print("Method\tTime")
    for (tp, var), values in sorted(result.items(), key=lambda x: x[0]):
        print(f"{tp} ({var})\t{mean(values):.5} (±{variance(values):.7})")
