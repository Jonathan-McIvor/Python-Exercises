# Create a new Python file and write a program that does the following:

# Write a program that determines the name of a shape from its number of sides
# Read the number of sides from the user and then report the appropriate name as part of a meaningful messages
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If a number of sides outside of 
# - this range is entered then your program should display an appropriate error message


numSides=int(input("How many sides in the shape: "))
geometry = {
    3: "The shape is a triangle.",
    4: "The shape is a quadrilateral.",
    5: "The shape is a pentagon.",
    6: "The shape is a hexagon.",
    7: "The shape is a heptagon.",
    8: "The shape is a octagon.",
    9: "The shape is a nonagon.",
    10: "The shape is a decagon.",
}
if numSides == 3:
  print(geometry[3])
elif numSides == 4:
  print(geometry[4])
elif numSides == 5:
  print(geometry[5])
elif numSides == 6:
  print(geometry[6])
elif numSides == 7:
  print(geometry[7])
elif numSides == 8:
  print(geometry[8])
elif numSides == 9:
  print(geometry[9])
elif numSides == 10:
  print(geometry[10])
else:
  print("Error, sides must be in between 3 and 10. Please try again.")
