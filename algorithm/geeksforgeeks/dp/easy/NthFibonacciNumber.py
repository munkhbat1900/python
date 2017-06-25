# http://practice.geeksforgeeks.org/problems/nth-fibonacci-number/0
# Nth Fibonacci Number
# O(log n) algorithm using matrix multiplication
# AC

from sys import stdin, stdout

def matrix_mul(a, b):
    c = [[0] * len(a) for i in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for p in range(len(a[0])):
                c[i][j] = (c[i][j] + a[i][p] * b[p][j]) % 1000000007
    
    return c

def matrix_power(n):
    a = [[1, 1], [1, 0]]
    ans = [[1, 0], [0, 1]]
    while n > 0:
        if (n & 1) == 1:
            ans = matrix_mul(ans, a)
        a = matrix_mul(a, a)
        n >>= 1
    return ans

def fib(n):
    c = matrix_power(n)
    return c[1][0]

if __name__ == '__main__':
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        stdout.write(str(fib(n)) + "\n")
