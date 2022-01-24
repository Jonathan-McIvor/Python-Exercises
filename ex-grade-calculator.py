# Create a new Python file and write a program that does the following:

    # Asks for an input from the user as a mark
    # If the mark is greater that 85 print "Distinction"
    # If the mark is between 65 and 85 print "Pass"
    # Anything else print "Fail"


# With use of elif

grade = int(input("Enter grade: "))

if grade >= 85:
    print("Distinction")
elif grade >= 65 and grade < 85:
    print("Pass")
else: 
    print("Fail")


#Without use of elif

ugrade =int(input("Enter awarded score: "))

if ugrade >= 85:
    print("Distinction")
if ugrade >= 65 and ugrade < 85:
    print("Pass")
if ugrade < 65:
    print("Fail")