"""
This program takes a decimal number and converts it into either binary,
hexidecimal or octal

"""
#ask user for a integer if not a integer remit error
decimal = int( input( "Please enter a number between 0 and 100: "))
if not (decimal >= 0 and decimal <= 100):
    print ("Invalid Number.")
    exit 


#ask user witch number. binary, hexidecimal or ocatal. if none remit error
base = int (input ("Pleqase enter 2 for binary or 8 for octal or 16 for hexadecimal: "))
if not (base ==2 or base ==8 or base ==16):
    print ("Invalid Number, must be 2, 8 or 16.")
    exit

#calculate binary hexidecimal or octal
value = ""
if decimal == 0:
    print ("all values are equal to 0")
    exit
newDecimal = decimal
if (base ==2 or base ==8):
    while (newDecimal != 0):
        value = str (newDecimal%base) + value
        newDecimal = newDecimal // base
    print("decimal = " +str(decimal) + " and in base "+ str(base)+ " = "+value)
else:
    while (newDecimal != 0):
        remainder = newDecimal%base
        if (remainder == 10):
            value = "a" + value
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

#display the ending value

    print("decimal = "+str(decimal)+" and in base "+str(base)+" = "+value)
           
#display the ending value
