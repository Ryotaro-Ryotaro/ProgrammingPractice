N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sum = [0]*(N+1)
for i in range(N):
    sum[i+1]  = sum[i] + A[i]

for _ in range(Q):
    L, R = map(int,input().split())
    hit_sum = sum[R] - sum[L-1]
    if hit_sum > (R-L+1 - hit_sum):
        print("win")
    elif hit_sum < (R-L+1 - hit_sum):
        print("lose")
    else:
        print("draw")
