name = open('mbox-short.txt')

ls = list()
counts = dict()

for line in name:
    if line.startswith('From:'):
        words = line.split()
        ls.append(words[1])

for word in ls:
    counts[word] = counts.get(word,0) + 1

max = None
w = None

for a,b in counts.items():
    if max is None or b > max:
        max = b
        w = a

print(w ,max)
