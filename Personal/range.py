#calculates range 




filename = input('Enter a file name: ')


infile = open(filename, 'r')

 
for line in infile:
    wordlist = line.split()

wordlist = [float(i) for i in wordlist]

first = wordlist[0]
last = wordlist[len(wordlist)-1]

ranger = last - first

print("Range: ", ranger)
