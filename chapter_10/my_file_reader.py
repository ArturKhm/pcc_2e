filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as file_object:
            # for line in file_object:
            #     print(line)
            # print(file_object.read())
            lines = file_object.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        # print(f"{filename} doesn't exist")
        pass
