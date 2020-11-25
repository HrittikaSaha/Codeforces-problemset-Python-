name = input()

checker = ''

for i in name:
    if i not in checker:
        checker = checker + i
        continue
if len(checker) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')