import re
phone_regex=re.compile(r'\+\d{12}')
email_regex=re.compile(r'\S+@\S+\.')

with open('example.txt','r') as f:
    for line in f:

        searchmatch=phone_regex.findall(line)
        for match in searchmatch:
            print(match)
        searchmatch=email_regex.findall(line)
        for match in searchmatch:
            print(match)