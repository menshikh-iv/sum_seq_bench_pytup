# Benchmarks for GIL talk (Pytup 24.11.18)

Intro
-----
**Slides:** [https://slides.com/menshikh_iv/gil_pain_pytup](https://slides.com/menshikh_iv/gil_pain_pytup)

**Requirements:** 
- `python >= 3.7`
- `cython >= 0.29`
- extras: 
    - `gcc`
    - `python3.7-dev`
    - etc


**Installation:** `python setup.py install`

**Benchmarking:** `python -c "from sum_seq import benchmark_sum_seq; benchmark_sum_seq()"`

Benchmark
---------
**Setup**

| key | value |
|-----|-------|
| OS | `Linux P50 4.15.0-36-generic #39-Ubuntu SMP Mon Sep 24 16:19:09 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux`|
| CPU | `Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz` |
| Python | `Python 3.7.0` |
| Settings | `n: 8, val: 200000000, iterations: 5` |

**Results**

| - | Time (sec) |
|---|------------|
| python (sequence) | `86.349` |
| python (thread) | `92.636` |
| python (process) | `22.646` |
| c (sequence) | `0.66055` |
| c (thread) | `0.18879` |
| c (process) | `0.20442` |
| cython (sequence)	| `0.65923`|
| cython (process) | `0.19117` |
| cython (thread) | `0.19168` |

