# this program calculates the mean from a txt


filename = input("enter a file: ")

with open(filename) as f:
    data = [float(line) for line in f]


first = float(input("Enter Starting temp: "))

second = float(input("Enter ending temp: "))


print("the diffrence is : ", second - first)
print("the sum is: ", sum(data))
