# This program inputs numbers from a txt and calculates the mean
#reads numbers horizontally 





filename = input('Enter a file name: ')


infile = open(filename, 'r')

sum = 0 
for line in infile:
    wordlist = line.split()
    
    for word in wordlist:
        
        amount = int(word)
        sum += amount
        
length = len(wordlist)       
average = sum / length

print('The mean is: ', average)

infile.close()






    
