fileWrite = open('Story.txt', 'w')          # 'w' is used to write file

print("Enter your Story here: ")

fileWrite.write("Your Story is: \n\n")

lines = []                                  # This can store multiple lines
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

fileWrite.write(text)

fileWrite.close()

fileRead = open('Story.txt', 'r')           # 'r' is used to read file
fileCon = fileRead.read()
print(fileCon)
fileRead.close()
