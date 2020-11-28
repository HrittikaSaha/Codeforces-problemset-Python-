n,h = input().split()
n,h = int(n), int(h)

s = input().split()

count = len(s)

for i in s:
    if int(i) > h:
        count = count + 1
        continue
print(count)