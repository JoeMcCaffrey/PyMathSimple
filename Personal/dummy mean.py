

filename = input('Enter a file name: ')


infile = open(filename, 'r')

sum = 0 
for line in infile:
    wordlist = line.split()
    
    for word in wordlist:
        
        amount = int(word)
        sum += amount
        
length = len(wordlist)       
mystery = sum / length

print('The mystery is: ', mystery)

infile.close()

