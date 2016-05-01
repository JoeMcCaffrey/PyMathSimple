# median

filename = input('Enter a file name: ')


infile = open(filename, 'r')


for line in infile:
    wordlist = line.split()

wordlist = [float(i) for i in wordlist]

length = 0
length = len(wordlist)
median = 0.0 

median2 = 0

if length %2 == 0:
    median = (wordlist[length//2]+ wordlist[(length//2)-1]) / 2.0
    print("Median: ",median)
else:
    median2 = wordlist[(len(wordlist)//2)]
    print("Median: ",median2)


print(wordlist) 
