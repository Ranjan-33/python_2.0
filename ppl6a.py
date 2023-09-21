#Write a python program to accept a file name from the user and perform the
#following operations
# Find the frequency of occurrence of the word accepted from the user in the file
import os.path
import sys

fname = input("Enter the filename: ")

if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

infile = open(fname, "r")
lineList = infile.readlines()

for i in range(20):
    if i< len(lineList):
        print(lineList[i])

word = input("Enter a word: ")
cnt = 0

for line in lineList:
    cnt += line.count(word)

print("The word", word, "appears", cnt, "times in the file")