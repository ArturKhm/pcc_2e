filenames = ['alice.txt', 'little_women.txt']
counter = ' a '
for filename in filenames:
    try:
        with open(filename) as file_object:
            # for line in file_object:
            #     print(line)
            # print(file_object.read())
            text = file_object.read()
            words = text.split()
            num_words = len(words)
            num_counter = text.count(counter)
        print(f"{num_words}, {num_counter}")
    except FileNotFoundError:
        # print(f"{filename} doesn't exist")
        pass