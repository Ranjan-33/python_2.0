#Develop a python program that could search the text in a file for phone numbers
#(+919900889977) and email addresses (sample@gmail.com)
import re
# Define the regular expression for phone numbers
phone_regex = re.compile(r'\+\d{12}')
# email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
email_regex = re.compile(r'\S+@\S+\.')
# Open the file for reading
with open('example.txt', 'r') as f:
# Loop through each line in the file
    for line in f:
# Search for phone numbers in the line
        searchmatch= phone_regex.findall(line)
# Print any matches found
        for match in searchmatch:
            print(match)
        searchmatch = email_regex.findall(line)
# Print any matches found
        for match in searchmatch:
            print(match)