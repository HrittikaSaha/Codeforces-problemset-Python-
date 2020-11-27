y = input()
main = str(int(y) + 1)

while True:
    if main.count(main[0])==1 and main.count(main[1])==1 and main.count(main[2])==1 and main.count(main[3])==1:
        print(main)
        break
    else:
        main = str(int(main) + 1)
        continue