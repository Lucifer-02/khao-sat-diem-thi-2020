file_char = open("unicode.txt", encoding= "utf8")

char_table = file_char.read().split("\n")


#print(len(char_table))
table = []
for code in char_table:
	table.append(code.split("\t"))

print(len(table))
print(table[0][1])

# file = open("test.txt", encoding= "utf8", mode= "w")

# file.write(str(char_table))

# for i in range(len(char_table)):
# 	data = data.replace(str(char_table[i][2:]), str(char_table[i][:1]))

# print(data)
# print(len(char_table))

# file = open("test.txt", "w")

# file.write(data)
