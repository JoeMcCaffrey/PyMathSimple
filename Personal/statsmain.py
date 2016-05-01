#This program is a collection of stats definitions
# 3.5 hours


from collections import Counter
import re


filename = input('Enter a file name: ')


infile = open(filename, 'r')

sum = 0 
for line in infile:
    wordlist = line.split()

wordlist = [float(i) for i in wordlist]
 
print("Original list: ",wordlist)

print("--------------------")



def swap(lyst, i , j):

    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp 



def bubblesort(wordlist):
    n = len(wordlist)

    while n > 1:
        i = 1
        while i < n :
            if wordlist[i] < wordlist[i-1]:
               swap( wordlist, i , i-1)
            i+= 1
        n -=1




bubblesort(wordlist)

print("Sorted List: ",wordlist)
print("--------------------")

def mean(wordlist):
    sum = 0

    for word in wordlist:
        
        amount = int(word)
        sum += amount
       # sum += word
        
    length = len(wordlist)       
    average = sum / length

    print('Mean: ', average)


def median(wordlist):
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


def mode(wordlist):
    data = Counter(wordlist)

    want = data.most_common(1)
    
    

    
    print("Mode: ",want)


def ranger(wordlist):
    first = wordlist[0]
    last = wordlist[len(wordlist)-1]

    ranger = last - first

    print("Range: ", ranger)


    
   

#wordlist = bubblesort(wordlist)

mean(wordlist)
median(wordlist)
mode(wordlist)
ranger(wordlist)
