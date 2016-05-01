# this program is a bubble sort from a txt file


def swap(lyst, i , j):

    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp 





filename = input("Enter a file name: ")


infile= open(filename,'r')


for line in infile:
    wordlist = line.split()

n = len(wordlist)

while n > 1:
    i = 1
    while i < n :
        if wordlist[i] < wordlist[i-1]:
            swap( wordlist, i , i-1)
        i+= 1
    n -=1

infile.close()         

print(wordlist) 
