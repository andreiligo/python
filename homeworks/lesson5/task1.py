list = []
while True:
    line = input("please enter data: ")
    if line == '':
        print(list)
        exit()
    else:
        new_line = line + '/n'
        list.append(new_line)

    with open("text1.txt", "w+") as text1_file:
        text1_file.writelines(list)
