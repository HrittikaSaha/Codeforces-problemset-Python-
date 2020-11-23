numbers = input()
numbers = int(numbers)
count = 0
 
for i in range(numbers):
    Petya,Vasya,Tonya = input().split()
    sum = int(Petya) + int(Vasya) + int(Tonya)
    if sum > 1:
        count = count + 1
        continue 
print(count)