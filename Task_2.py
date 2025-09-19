file = open("output.txt", "w")

data = input("Enter text to write to the file: ")

file.write(data)
print("Data successfully written to output.txt\n")

add_data = input("Enter additional text to append: ")

file.write("\n")
file.write(add_data)
print("Data successfully appended.\n")

file.close()

file = open('output.txt', 'r')

readFile = file.read(-1)
print("Final content of output.txt:")
print(readFile)

file.close()
