#Write a Python program to read first n lines of a file. 

n = int(input("\n\t\tEnter Lines To Read : "))
f = open("myfile.txt","r")
for i in range(n):
	print(f.readline())
