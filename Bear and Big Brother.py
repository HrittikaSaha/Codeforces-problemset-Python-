a,b = input().split()
a,b = int(a),int(b)
count = 0

while True:
    count = count + 1
    a = 3 * a
    b = 2 * b
    if a > b:
        break
    else:
        continue
print(count)