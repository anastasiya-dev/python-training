name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dct = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5].split(':')
    dct[time[0]] = dct.get(time[0], 0) + 1
newlist = sorted([(k,v) for k,v in dct.items()])
for k,v in newlist:
    print(k,v)