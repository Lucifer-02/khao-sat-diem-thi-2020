import csv

file = open("raw_data.txt", "r")

# Read first student
datas = file.read().split("\n")

file = open("clean_data.csv", encoding="utf8", mode="w")

sbd = 2000000

for data in datas:
    try:

        sbd += 1
        sbd_str = "0" + str(sbd)

        # make data becomes a list
        data = data.split("\\n")

        # remove \r and \t
        for i in range(len(data)):
            data[i] = data[i].replace("\\r", "")
            data[i] = data[i].replace("\\t", "")

        # remove tags
        for i in range(len(data)):
            tags = []
            for j in range(len(data[i])):
                if data[i][j] == "<":
                    begin = j
                if data[i][j] == ">":
                    end = j
                    tags.append(data[i][begin:end + 1])

            for tag in tags:
                data[i] = data[i].replace(tag, "")

        # remove space
        for i in range(len(data)):
            data[i] = data[i].strip()

        unempty_line = []

        for i in range(len(data)):
            if data[i] != "":
                unempty_line.append(data[i])

        data = unempty_line

        # choose name, date of birth and score lines then convert special char
        name = data[7]
        dob = data[8]
        score = data[9]

        for i in range(len(name)):
            if name[i:i + 2] == "&#":
                name = name[:i] + chr(int(name[i + 2:i + 5])) + name[i + 6:]

        for i in range(len(score)):
            if score[i:i + 2] == "&#":
                score = score[:i] + \
                    chr(int(score[i + 2:i + 5])) + score[i + 6:]

        # convert special char to normal char
        # create unicode table
        file_char = open("unicode.txt", encoding="utf8")

        char_table = file_char.read().split("\n")

        table = []
        for code in char_table:
            table.append(code.split("\t"))

        # convert special char for name and score lines
        for i in range(len(table)):
            name = name.replace(table[i][1], table[i][0])

        for i in range(len(table)):
            score = score.replace(table[i][1], table[i][0])

        # covert upper to lower char
        name = name.lower()
        score = score.lower()

        # change dob
        dob = dob.split("/")
        dd = int(dob[0])
        mm = int(dob[1])
        yy = int(dob[2])

        # store to data
        data = [sbd_str, name.title(), str(dd), str(mm), str(yy)]

        # score list process
        score = score.replace(":", "")
        score = score.replace("khtn", "khtn  ")
        score = score.replace("khxh", "khxh  ")

        score_list = score.split("   ")

        for subject in ["toán", "ngữ văn", "khxh", "khtn", "lịch sử", "địa lí", "gdcd", "sinh học", "vật lí", "hóa học", "tiếng anh"]:
            if subject in score_list:
                data.append(
                    str(float(score_list[score_list.index(subject) + 1])))
            else:
                data.append("-1")

        # write data to test.txt
        with open("clean_data.csv", "a", encoding="utf8", newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(data)
    except:
        print(sbd_str)
