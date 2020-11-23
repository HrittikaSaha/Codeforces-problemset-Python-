a = input()
a = int(a)
 
for i in range(a):
    word = input()
    if len(word) > 10:
        print(word[0]+str(len(word[1:-1]))+word[-1])
    else:
        print(word)  