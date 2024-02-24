#Write a Python program to append text to a file and display the text.

f = open("myfile.txt", "a")
f.write("Now the file has more content!")
f.close()


f = open("myfile.txt", "r")
print(f.read())
