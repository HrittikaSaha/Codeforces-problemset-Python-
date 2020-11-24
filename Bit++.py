numbers = input()
numbers = int(numbers)
count = 0

for i in range(numbers):
    x = input()
    if x == '++X' or x == 'X++':
        count = count + 1
        continue
    else:
        count = count - 1
        continue
print(count)

