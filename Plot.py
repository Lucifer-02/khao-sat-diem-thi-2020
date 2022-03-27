# read file 
with open("clean_data.csv", encoding="utf8") as file:
	data = file.read().split('\n')

# Save to
header = data[0]
students = data[1:]
 
header = header.split(',')

# split ech student in list
for i in range(len(students)):
	students[i] = students[i].split(",")
	

print(students[2])