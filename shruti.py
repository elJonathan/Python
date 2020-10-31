l= None
s= None
list = []
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue
    list.append(num)
print(list)
for j in range(0, len(list)):
    list[j] = int(list[j])
l=list[0]
s=list[0]
for i in list:
  if s>i:
    s=i
  if l<i:
    l=i;
print("MAX: ",l)
print("MIN: ",s)
