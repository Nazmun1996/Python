import re
try:
    with open('GUTINDEX.ALL') as myfile:
        data = myfile.read()
        x = input("Enter Search String:")
        for record in re.split('\n *\n', data):
            words = record.strip()
            words = re.sub(r"\s+"," ", words)
            if x in words:
                print(words+'\n')
           
except FileNotFoundError:
    print("File do not exist")
