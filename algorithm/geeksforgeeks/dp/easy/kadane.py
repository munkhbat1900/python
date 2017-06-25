# http://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
# kadane's algorithm
# accepted Execution Time:0.08
from sys import stdin, stdout
if __name__ == '__main__':
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        arr = [int(i) for i in stdin.readline().split()]
        max_va = -1000
        s = 0
        for x in arr:
            s += x
            max_va = max(s, max_va)
            if s < 0:
                s = 0
        stdout.write(str(max_va) + "\n")