### WRITE/READ TO TEXT FILE

## WRITE
# Create a new empty text file
file = open("data.txt", "w") # w: write mode

# write 0-9 to data.txt
for i in range(5):
	file.write("Number " + str(i) + "\n")

file = open("data.txt", "a") # a: append mode
for i in range(5,10):
	file.write("Number " + str(i) + "\n")

## READ
file = open("data.txt", "r") # r: reading

# read to a list
lines = file.read().split("\n")

# iterate (loop) through the list
for i in range(len(lines)):
	print("Line " + str(i) + ": " + lines[i])

### OUTPUT:
# Line 0: Number 0
# Line 1: Number 1
# Line 2: Number 2
# Line 3: Number 3
# Line 4: Number 4
# Line 5: Number 5
# Line 6: Number 6
# Line 7: Number 7
# Line 8: Number 8
# Line 9: Number 9
# Line 10: