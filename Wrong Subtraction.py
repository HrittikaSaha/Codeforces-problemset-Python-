n,k = input().split()
k = int(k)
ans = int(n)
a = 1
while a <= int(k):
    if ans%10 == 0:
        ans = ans / 10
    else:
        ans = ans -1
    a = a + 1
print(int(ans))