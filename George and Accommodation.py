n = input()
count = 0

for i in range(int(n)):
    a,b = input().split()
    if int(b) - int(a) >= 2:
        count = count + 1
print(count)