# 3. Write to a File
# Write a program to create a text file and write some content to it.
# Using file functions like write and open.

file = open("example.txt", "w")
file.write("Line 1 Writing to file.\n")
file.write("Line 2 Writing to file.\n")
file.write("Writing to a file using Python is easy!")
file.close()

print("Content written successfully.")