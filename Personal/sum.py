# this program finds the sum from a txt file
#reads numbers horizontally


filename = input('Enter a file name: ')


infile = open(filename, 'r')

sum = 0

for line in infile:
    wordlist = line.split()
    for word in wordlist:
        number = int(word)
        sum += number

print("the sum is: " , sum)
