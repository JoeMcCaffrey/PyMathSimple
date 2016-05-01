
"""
This program asks the user for an integer between 0 and 255, converts the
value into a different base and displays.

by Mahadev
"""
decimal = int(input("please enter an integer between 0 and 255: "))
if  not(decimal >= 0 and decimal <= 255):
    print("Wrong number.  So quitting")
    exit
base = int(input("please enter 2 for binary or 8 for octal or 16 for hex: "))
if not(base == 2 or base == 8 or base == 16):
    print("Must be 2, 8 or 16.  Quitting")
    exit
value = ""
if decimal == 0:
    print("all values are equal to 0")
    exit
newDecimal = decimal
if (base == 2 or base == 8):
    while(newDecimal != 0):
        value = str(newDecimal%base)+value
        newDecimal = newDecimal//base
    print("decimal = "+str(decimal)+" and in base "+str(base)+" = "+value)
else:
    while(newDecimal != 0):
        remainder = newDecimal%base
        if (remainder == 10):
            value = "a"+value
        elif (remainder == 11):
            value = "b"+value
        elif (remainder == 12):
            value = "c"+value
        elif (remainder == 13):
            value = "d"+value
        elif (remainder == 14):
            value = "e"+value
        elif (remainder == 15):
            value = "f"+value
        else:
            value = str(remainder)+value
        newDecimal = newDecimal//base
    print("decimal = "+str(decimal)+" and in base "+str(base)+" = "+value)
           
        
    
