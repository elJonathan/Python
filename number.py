a = 9278
c = str(a)
b = len(c)

number = []
for i in range (1, b+1):
    j = a % (10**i)
    number.append(j)
print(number)
