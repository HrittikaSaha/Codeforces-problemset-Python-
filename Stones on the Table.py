n = int(input())
s = input()
count = 0
o = ''

for i in range(n-1):
    if s[i] == s[i+1]:
        count = count + 1
print(count)