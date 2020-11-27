s = input()
t = input()
a = -1
o = ''

if len(s) != len(t):
    print("NO")
else:
    for i in range(len(s)):
        o = o + t[a]
        a = a - 1
    if o == s:
        print('YES')
    else:
        print('NO')