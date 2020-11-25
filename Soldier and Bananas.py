k,n,w = input().split()
k,n,w = int(k),int(n),int(w)
a = 1

total = 0


while a <= w:
    total = total + (k*a)
    a += 1

if total <= n:
    print(0)
else:
    print(total - n)