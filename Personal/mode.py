# this calculates mode

from collections import Counter

filename = input('Enter a file name: ')


infile = open(filename, 'r')

for line in infile:
    wordlist = line.split()

wordlist = [float(i) for i in wordlist]

data = Counter(wordlist)

want = data.most_common(1)




print("Mode: ",want)


