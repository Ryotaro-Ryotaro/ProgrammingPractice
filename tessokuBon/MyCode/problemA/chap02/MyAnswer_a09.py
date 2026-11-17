H, W, N = map(int, input().split())
Kingdom = [[0]*(W+1) for _ in range(H+1)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    Kingdom[A-1][B-1] += 1
    Kingdom[A-1][D] -= 1
    Kingdom[C][B-1] -= 1
    Kingdom[C][D] += 1
prefix = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + Kingdom[i][j]
for i in range(1, H+1):
    print(*prefix[i][1:])