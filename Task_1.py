try:
    file = open("sample.txt", "r+")

    print("Reading file content:")
    Line_1 = file.readline().strip()
    Line_2 = file.readline().strip()

    print(f"Line 1: {Line_1}\nLine 2: {Line_2}")

except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found.")
