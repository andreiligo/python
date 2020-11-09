with open("text2.txt") as file_text:
    line_count = 0
    words = 0
    for line in file_text:
        line_count += 1
        words += len(set(line.split()))


print(line_count)
print(words)