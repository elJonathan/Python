largest = None
smallest = None
list = []
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    list.append(num)

for i in list:
    if smallest is None or largest is None:
        smallest = i
        largest = i
    elif i < smallest:
        smallest = i

for j in list:
    if largest is None:
        largest = j
    elif j > largest:
        largest = j

print("Maximum is " ,largest)
print("Minimum is " ,smallest)
