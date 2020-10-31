
l=['hello', 'hi', 'hello']
l1=[]
for i in range(0, len(l)):
   for j in range(i+1, len(l)):
       if l[i]!=l[j]:
           l1.append(l[i])
print(l1)
