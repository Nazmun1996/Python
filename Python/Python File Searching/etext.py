import re

def search_by_etext():


    with open("GUTINDEX.ALL") as f:
        for line in f:
            match = re.search(r"\s(\d+)$", line.strip())
            if match:
                x = input("Enter ETEXT NO:")
                if x in match.group(1):
                    print (line)
            
search_by_etext()
