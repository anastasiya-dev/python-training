name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
names = dict()

for line in handle:
    if not line.startswith("From "): 
        continue
    words = line.split()
    names[words[1]] = names.get(words[1],0) + 1

mname = None
mcount = None
for name,count in names.items():
    if mcount is None or count > mcount:
        mname = name
        mcount = count
print(mname, mcount)