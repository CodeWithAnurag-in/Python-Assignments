user_inp1 = input("Enter text to write to the file: ")
with open("output.txt", "r+") as file:
    write_file = file.write(user_inp1 + "\n")
    file.close()
print("Data succesfully written to output.txt.")

print(" ")

user_inp2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    append_file = file.write(user_inp2 + "\n")
    file.close()
print("Data succesfully appended.")

print(" ")

print("Final content of output.txt" )

with open("output.txt", "r") as file:
    read_file = file.read()
    print(read_file)
    file.close()