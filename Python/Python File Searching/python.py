import re

def search_by_etext():
    
    fhand = open('GUTINDEX.ALL')
    print("Search by ETEXT:")

    for line in fhand:
        if not re.match(r'^\s', line) and not line.startswith("~"):
            if not line.startswith(" ") and not line.startswith("TITLE"):
                    words = line.rstrip()
                    words = line.lstrip()
                    words = words[-7:]
                    if not words.startswith("X"):
                        print (words)



def search_by_title():

    fhand = open('GUTINDEX.ALL')
    print("Search by Title:")

    for line in fhand:
        if not line.startswith(" [") and not line.startswith("﻿TITLE") and not line.startswith("~"):
            if not line.startswith(" ") and not line.startswith("TITLE") and not line.startswith(" [Language: French]"):
                words = line.rstrip()
                words = line.lstrip()
                words = words[:-6]
                if ", by" in words:
                    words = words[0:words.find(', by')]
                    print (words)
                else:
                    words = words[0:words.find(',')]
                    print (words)



def search_by_author():

    fhand = open('GUTINDEX.ALL')
    book_info = ''

    for line in fhand:
        line = line.rstrip()

        if (line.startswith('TITLE') or line.startswith('~')):
            continue

        if (len(line) == 0):
            book_info = re.sub(r'\[.*$', '', book_info)

            if ('by ' in book_info):
                tokens = book_info.split('by ')
            else:
                tokens = book_info.split(',')

            if (len(tokens) > 1):
                authors = tokens[-1].strip()
                print(authors)

            book_info = ''

        else:
            
            line = re.sub(r'\d+$', '', line)
            book_info +=  ' ' + line.rstrip()



    

print ("CSE 425 ASSIGNMENT IN PYTHON\n".center(80))
print ("Press 1 to Search by ETEXT NO.\n")
print ("Press 2 to search by Title\n")
print ("Press 3 to Search by Author Name\n")


x = int(input("\n\nPlease enter your value: "))
if x ==1:
    search_by_etext()
elif  x ==2:
    search_by_title()
elif x ==3:
    search_by_author()
else:
    print ("INVALID INPUT")

