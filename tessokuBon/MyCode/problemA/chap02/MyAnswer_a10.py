N = int(input())
A = list(map(int, input().split()))
D = int(input())

prefix_right_list = [0]
prefix_left_list = [0]
max_value = A[0]
for i in range(N):
    max_value = max(max_value, A[i])
    prefix_left_list.append(max(A[i], max_value))
    ##prefix_left_listには左から出発したときのそれまでの最大値を左から順に入れている。
max_value = A[0]
for i in range(N):
    max_value = max(A[N - i - 1], max_value)
    prefix_right_list.insert(0, max_value)
    ##prefix_right_listには右から出発したときのそれまでに最大値を右から順に入れている。

for _ in range(D):
    L, R = map(int, input().split())
    answer = max(prefix_left_list[L - 1], prefix_right_list[R])
    print(answer)
