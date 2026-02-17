# Day 6 - File Handling

# Write to a file
with open("sample1.txt", "w") as f:
    f.write("Hello, this is Day 6 file handling practice.\n")
    f.write("Learning Python for AI & ML.\n")

# Read from the file
with open("sample1.txt", "r") as f:
    content = f.read()
    print(content)

# Append data to file
with open("sample1.txt", "a") as f:
    f.write("This line is appended.\n")

#read line by line
with open("sample1.txt", "r") as f:
    for line in f:
        print(line.strip())
