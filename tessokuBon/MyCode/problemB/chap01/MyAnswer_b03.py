N = int(input())
A = list(map(int, input().split()))

answer = "No"
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if i + j + k == 1000:
                answer = "Yes"
                break
print(answer)