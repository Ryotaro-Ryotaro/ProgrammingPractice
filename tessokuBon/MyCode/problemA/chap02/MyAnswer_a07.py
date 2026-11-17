D = int(input())
N = int(input())
prefix = [0]*(D+2)
for _ in range(N):
    L, R = map(int, input().split())
    prefix[L] += 1
    prefix[R+1] -= 1
sum = [0]*(D+1)
for i in range(D):
    sum[i+1] = sum[i] + prefix[i+1]
for i in range(D):
    print(sum[i+1])
