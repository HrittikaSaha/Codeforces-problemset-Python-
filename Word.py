s = input()

up_count = 0
low_count = 0

for i in s:
    if i.isupper() == True:
        up_count = up_count + 1
    else:
        low_count = low_count + 1
if up_count > low_count:
    print(s.upper())
else:
    print(s.lower())