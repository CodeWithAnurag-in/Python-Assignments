with open("sample.txt", "r") as f:
    read_file = f.readline()
    print(read_file)
    read_file = f.readline()
    print(read_file)
    f.close()