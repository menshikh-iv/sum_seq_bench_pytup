#include "sum_seq.h"

unsigned long long int sum_seq(unsigned long long int n) {
    unsigned long long int result = 0, i = 0;

    for (;i < n; i++) {
        result += i;
    }

    return result;
}
