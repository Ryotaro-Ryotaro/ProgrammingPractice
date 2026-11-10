N, X = map(int, input().split())
A = list(map(int, input().split()))

answer = "No"
for i in range(N):
    if A[i] == X:
        answer = "Yes"
        break
print(answer)