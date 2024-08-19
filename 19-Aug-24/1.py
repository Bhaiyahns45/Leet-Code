def nthUglyNumber(n: int) -> int:

    ugly_number = 1
    i = 1
    two = 1
    three = 1
    five = 1

    while i != n:

        ugly_number = min(2 * two, 3 * three, 5 * five)

        if ugly_number == 2 * two:
            two += 1
        if ugly_number == 3 * three:
            three += 1
        if ugly_number == 5 * five:
            five += 1

        i += 1
        print(ugly_number)
    return i


def nthUglyNumber1(n: int) -> int:

    if n <= 0:
        return 0
    if n == 1:
        return 1

    t2 = t3 = t5 = 0
    k = [0] * n
    k[0] = 1

    for i in range(1, n):
        k[i] = min(k[t2] * 2, k[t3] * 3, k[t5] * 5)

        if k[i] == k[t2] * 2:
            t2 += 1
        if k[i] == k[t3] * 3:
            t3 += 1
        if k[i] == k[t5] * 5:
            t5 += 1

    return k[-1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        if n <= 0:
            return 0
        if n == 1:
            return 1

        t2 = t3 = t5 = 0
        k = [0] * n
        k[0] = 1

        for i in range(1, n):
            k[i] = min(k[t2] * 2, k[t3] * 3, k[t5] * 5)

            if k[i] % 2 == 0:
                t2 += 1
            if k[i] % 3 == 0:
                t3 += 1
            if k[i] % 5 == 0:
                t5 += 1

        return k[-1]


nthUglyNumber1(17)
# nthUglyNumber(17)
