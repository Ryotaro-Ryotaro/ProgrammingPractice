N = str(input())
N_list = []

##8ケタの配列になるように先頭に０を長さの足りない分を付け加えている。
margin = 8 - len(N)
for i in range(margin):
    N_list.append(0)

for i in range(len(N)):
    N_list.append(int(N[i]))

answer = 0
index_list = [7,6,5,4,3,2,1,0]
for i in range(len(N_list)):
    answer = answer + N_list[i]*(2**index_list[i])
print(answer)