# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox-short.txt')
#fname = input("Enter file name: ")
#fh = open(fname)
count = 0
s = 0


for line in fh:
    if line.startswith('X-DSPAM-Confidence:') :
        count = count + 1
        pos = line.find(' ')
        num = line[pos + 1:]
        n = float(num)
        s = s + n

print(s/count)
