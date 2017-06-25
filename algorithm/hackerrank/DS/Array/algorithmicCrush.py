# https://www.hackerrank.com/challenges/crush/problem
# Algorithmic Crush 
# accepted 
from sys import stdin, stdout

if __name__ == '__main__':
    n, m = [int(i) for i in stdin.readline().split()]
    arr = [0] * n
    for i in range(m):
        a, b, k = [int(i) for i in stdin.readline().split()]
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    
    val = 0
    ans = 0
    for i in range(n):
        val += arr[i]
        ans = max(ans, val)
        #arr[i] = val
    stdout.write(str(ans))