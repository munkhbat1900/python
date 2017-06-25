# http://practice.geeksforgeeks.org/problems/ugly-numbers/0
# ugly numbers
# dynamic programming easy
# AC Execution Time:0.081

from sys import stdin, stdout

def find_ugly(n):
    uglies = [0] * (n + 1)
    uglies[0] = 1
    i2 = 0
    i3 = 0
    i5 = 0
    next_factor_2 = 2
    next_factor_3 = 3
    next_factor_5 = 5

    for i in range(1, n + 1):
        m = min(next_factor_2, next_factor_3, next_factor_5)
        uglies[i] = m
        if m == next_factor_2:
            i2 += 1
            next_factor_2 = 2 * uglies[i2]

        if m == next_factor_3:
            i3 += 1
            next_factor_3 = 3 * uglies[i3]

        if m == next_factor_5:
            i5 += 1
            next_factor_5 = 5 * uglies[i5]

    return uglies

if __name__ == '__main__':
    uglies = find_ugly(501)
    t = int(stdin.readline())
    # print(uglies)
    for p in range(t):
        n = int(stdin.readline())
        stdout.write(str(uglies[n - 1]) + "\n")