N, X = map(int, input().split())
A = list(map(int, input().split()))
left = 0
right = N - 1
mid = (left + right) // 2
answer = 0
while left <= right:
    if A[mid] < X:
        left = mid + 1
        mid = (left + right) // 2
    elif A[mid] > X:
        right = mid - 1
        mid = (left + right) // 2
    else:
        answer = mid
        break
print(answer + 1)
