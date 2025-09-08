name = input("Enter file name: ")
try:
    fname = open(name,'r')
except:
    print("File ", name, " couldn't be found:(")
    exit()
words = dict()
for line in fname:
    temp = line.split()
    for word in temp:
 #       if word not in words:
 #       else:
 #           words[word] = words[word] + 1
        words[word] = words.get(word, 0) + 1

max_word = None
max_freq = None
for word,freq in words.items():
    if max_freq == None or freq > max_freq:
        max_word = word
        max_freq = freq
print("The most common word", max_word, "is used", max_freq, "times.")
