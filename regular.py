import re

x = open('regex_sum_860526.txt')
sum = 0
line = x.read().replace("\n"," ")
y = re.findall('[0-9]+', line)

for i in y:
    i = int(i)
    sum = sum + i

print(sum)
