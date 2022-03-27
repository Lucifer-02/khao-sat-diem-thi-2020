file = open("unicode.txt", "r")

data = file.read()

# for i in range(len(data)):
# 	data[i] = data[i][7:]
# 	data[i] = data[i].replace('\\', '-1')
# 	data[i] = data[i].replace('\\t', '')
# 	data[i] = data[i].replace('-1', '\\')


# print(data[0:17])
# print(data[18:35])
# print(data[36:53])

temp = ""
for i in range(512):
	temp = temp + data[i*18+7:i*18+17] + "m"

data = temp

data = data.split("m")
print(len(data))
print(data)
# file = open("data.txt", "w")

# file.write(str(data))