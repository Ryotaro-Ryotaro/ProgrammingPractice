N, K  = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

answer = "No"
for i in range(N):
    for j in range(N):
        if i + j == K:
            answer = "Yes"
            break
print(answer)

##i,jをそのまま比べるのではなくlistのi,j番目を比べる。