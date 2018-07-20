import re

def search_by_author():

    fhand = open('GUTINDEX.ALL')
    book_info = ''
    for line in fhand:
        line = line.rstrip()

        if (line.startswith('TITLE') or line.startswith('~')):
            continue
        
        if (len(line) == 0):
            # remove info in square bracket from book_info
            book_info = re.sub(r'\[.*$', '', book_info)

            if ('by ' in book_info):
                tokens = book_info.split('by ')
            else:
                tokens = book_info.split(',')

            if (len(tokens) > 1):
                authors = tokens[-1].strip()
                x = input("Author Name:")
                if x in authors():
                    print (line)
                book_info = ''

        else:
            # remove ETEXT NO. from line
            line = re.sub(r'\d+$', '', line)
            book_info +=  ' ' + line.rstrip()
            

search_by_author()
