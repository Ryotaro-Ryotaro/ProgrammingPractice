A, B = map(int, input().split())

answer = "No"
for i in range(A, B-1):
    if 100 % i == 0:
        answer = "Yes"
        break
print(answer)
# ##range(A, B, C)
# Aは始まりの値、Bは終わりの値、よってBになったら終わるから上の書き方ではiはA,A+1,...,B-1で終わる
# Bまで調べたいなら終わりの値をB+1にすべき
# Cは間隔の値、デフォルトでは１