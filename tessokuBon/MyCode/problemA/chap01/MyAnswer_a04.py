N = int(input())

answer = [0]*10
n = 0
while N > 0:
    while N >= 2**(n+1):
        n = n + 1
    answer[9-n] = 1
    N = N - 2**n
    n = 0
answer_number = "".join(map(str, answer))
print(answer_number)

##難しかった。もう一度自分で解いてみた方がいい。