#fname = input("Enter file name: ")
fh = open('romeo.txt')
list = []
ls = []
for line in fh:
    words = line.split()
    list = list + words
print(list)
print(len(list))

for i in list:
   if i not in ls:
       ls.append(i)
print(ls)
