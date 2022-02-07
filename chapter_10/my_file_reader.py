filename = 'learning_python.txt'
with open(filename) as file_object:
    # for line in file_object:
    #     print(line)
    # print(file_object.read())
    lines = file_object.readlines()
for line in lines:
    print(line.strip().replace('Python', 'C'))
