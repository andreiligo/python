file1 = open("text3.txt", "w", encoding="utf-8")
file2 = open("text3_2.txt", "w", encoding="utf-8")
num_dict = {'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'}
new_string = ''
for line in file1:
    word = line.split()[0]
    new_string += line.replace(word, num_dict.value(word))

file2.write(new_string)

file1.close()
file2.close()
