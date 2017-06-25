# https://www.hackerrank.com/challenges/array-left-rotation
# hackerrank Left Rotation
# accepted 
from sys import stdin, stdout

n, d = [int(x) for x in stdin.readline().rstrip().split()]
a = [int(x) for x in stdin.readline().rstrip().split()]

ls = a[d:] + a[0:d]
ans = " ".join(str(x) for x in ls)
stdout.write(ans)
