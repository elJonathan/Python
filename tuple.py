name = open('mbox-short.txt')

ls = list()
dali = list()
hol = list()

dat = dict()

for line in name:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            ls.append(words)

#print(ls)

for l in ls:
    new = l[5]
    dali.append(new)

#print(dali)

for d in dali:
    hr = d.split(':')
    hol.append(hr[0])

#print(hol)

for da in hol:
    dat[da] = dat.get(da , 0) + 1

#print(dat)

tada = sorted(dat.items())

#print(tada)

for x,y in tada:
    print(x,y)
