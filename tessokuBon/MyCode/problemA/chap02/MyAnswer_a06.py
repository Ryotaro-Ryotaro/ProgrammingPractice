N, Q = map(int, input().split())
A = list(map(int, input().split()))

presum = [0]*(N+1)
for i in range(N):
    presum[i+1] = presum[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    answer = presum[R] - presum[L-1]
    print(answer)