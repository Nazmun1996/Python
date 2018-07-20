import re

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
                    x = input("Search by title")
                    for x in words:
                        print (line)
                else:
                    words = words[0:words.find(',')]
                    x = input("Search by title")
                    for x in words:
                        print (line)
search_by_title()
