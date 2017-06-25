# http://practice.geeksforgeeks.org/problems/ncr/0
# nCr
# Binomial Coefficient
# execution time exceeds. same java algorithm is accepted.
# java code excutes 0.09 sec
# python exceeds 0.924sec

from sys import stdin, stdout

memo=[]

def topdown(n, r):
    if r == 0 or r == n :
        return 1
    if (memo[n][r] != -1):
        return memo[n][r]
    
    memo[n][r] = (topdown(n - 1, r - 1) + topdown(n - 1, r)) % (10 ** 9 + 7)
    return memo[n][r]

def bottomup(n, r):
    dp = [[0] * (r + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(r, i) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % (10 ** 9 + 7)
    return dp[n][r]

if __name__ == '__main__':
    t = int(stdin.readline())
    for i in range(t):
        n, r = [int(i) for i in stdin.readline().split()]
        if n < r:
            stdout.write("0\n")
            continue
        memo = [[-1] * (r + 1) for i in range(n + 1)]
        stdout.write(str(topdown(n ,r)) + "\n")