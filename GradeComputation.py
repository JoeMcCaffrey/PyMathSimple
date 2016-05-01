"""
This program asks a user for a name and a score and displays the letter grade /n
in a output.txt file


"""
# First make a file called output.txt
# ask user for a number and round it, store it and the students name
f= open( "output.txt", 'w')
f.write ( "|%12s|%8s|%8s|\n" % ("Name", "Score", "Grade" ) )
f.write ("--------------------------------\n")


while True :
    
    student = input("Please enter students name or empty line to stop: ")
    if (student == ""):
        break 
    score = round (float(input("Please enter the score: ")))



# set the grades from the score input


    if (score < 0):
        grade = "invalid"
    elif (score < 60):
        grade = "F"
    elif (score < 70):
        grade = "D"
    elif (score < 80):
        grade = "C"
    elif (score < 90):
        grade = "B"
    elif (score <= 100):
        grade = "A"
    else:
        grade = "invalid"
#print the grades, name and score in the .txt file 
    

    f.write ("|%12s|%8s|%8s|\n" % (student,score, grade ))
f.close ()

    
