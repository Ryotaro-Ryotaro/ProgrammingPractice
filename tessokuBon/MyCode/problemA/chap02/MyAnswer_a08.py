H, W = map(int, input().split())
A = []
for i in range(H):
    Wlist = list(map(int, input().split()))
    A.append(Wlist)
prefixList = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        prefixList[i+1][j+1] = A[i][j] + prefixList[i][j+1] + prefixList[i+1][j] - prefixList[i][j]
Q = int(input())
for _ in range(Q):
    A, B, C, D = map(int, input().split())
    answer = prefixList[C][D] - prefixList[A-1][D] - prefixList[C][B-1] + prefixList[A-1][B-1]
    print(answer)