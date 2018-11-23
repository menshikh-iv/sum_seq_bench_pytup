def sum_seq(n):
    cdef long long unsigned int result = 0, i = 0;
    cdef long long unsigned int n_internal = n;

    with nogil:
        for i in range(n_internal):
            result += i

    return result
