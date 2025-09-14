import re

fhandle = open("regex_sum.txt")
sum = 0
count = 0
for line in fhandle:
    num = re.findall('[0-9]+', line)
    if len(num) == 0 : continue
    for number in num:
        sum = sum + int(number)
        count = count + 1

print(sum, count)