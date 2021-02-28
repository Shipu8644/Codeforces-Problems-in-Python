n, k = map(int, input().split())
maxdist = 0
n1 = list(map(int, input().split()))
n1.sort()
# print(*n1,sep=" ")
maxdist = 2 * max(n1[0], k - n1[n - 1]);
# print(maxdist)
for i in range(0, n - 1):
    maxdist = max(maxdist, n1[i + 1] - n1[i])



print("{0:.10f}".format(maxdist/2))