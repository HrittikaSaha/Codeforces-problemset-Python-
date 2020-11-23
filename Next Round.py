n,k = input().split()
n = int(n)
k = int(k)

numbers = input().split()
new = []
count = 0

for u in numbers:
    new.append(int(u))

for h in new:
    if h > 0 and h >= new[k-1]:
        count = count + 1
        continue
print(count)