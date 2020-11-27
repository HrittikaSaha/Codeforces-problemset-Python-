n = input()
n_list = []
help = [4 , 7]
 
for i in n:
    n_list.append(int(i))
 
count_4 = n_list.count(4)
count_7 = n_list.count(7)
 
if (count_7 + count_4) in help:
    print('YES')
else:
    print('NO')