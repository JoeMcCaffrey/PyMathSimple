"""
This program selects a random integer from [0,255]. then display in decimal
binary, octal and hexidecimal 10 times

By: Joe McCaffrey
"""

#display the heading to the table

print( "%8s %8s %8s %8s" % ("Decimal", "Binary", "Octal", "Hex"))
print("------------------------------------")
#get 10 random numbers


import random
for x in range (10):
    decimal = random.randint (0,255)
    newDecimal= decimal 
    base = 2
    binaryValue= ""
    if decimal == 0 :
        print ("0") 
    
#convert the 10 numbers 10 times for binary
    while (newDecimal !=0):
        
        
        binaryValue = str (newDecimal%base)+ binaryValue
        newDecimal = newDecimal//base
       
    
#convert the 10 numbers 10 times for octal
    octalValue=""
    base = 8
    newDecimal=decimal
    if decimal == 0 :
        print ("0")
    while (newDecimal !=0):
        
        
        octalValue = str (newDecimal%base)+ octalValue
        newDecimal = newDecimal//base
    
#convert the 10 numbers 10 times for hexidecimal
    hexValue =""
    base = 16
    newDecimal=decimal
    if decimal == 0 :
        print ("0")
    while (newDecimal !=0):
        remainder = newDecimal%base
        if (remainder == 10):
            hexValue = "a"+hexValue
        elif (remainder == 11):
            heValue = "b"+hexValue
        elif (remainder == 12):
            hexValue = "c"+hexValue
        elif (remainder == 13):
            hexValue = "d"+hexValue
        elif (remainder == 14):
            hexValue = "e"+hexValue
        elif (remainder == 15):
            hexValue = "f"+hexValue
        else:
            hexValue = str(remainder)+hexValue
        newDecimal = newDecimal//base

#display all converted numbers in table
    
    print( "%8d%10s%8s%8s" % (decimal,binaryValue,octalValue,hexValue))
