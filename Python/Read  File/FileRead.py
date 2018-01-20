#This program this file.txt and counts the nunmber of words in it
#FileRead.py and file.txt both files need to be under same directory

pfile = open('file.txt','r')

text = pfile.read()

words = text.split()

counts = dict()
for word in words:
    counts[word]= counts.get(word,0)+1
    big_count = None
    big_word = None
    for word, count in counts.dict():
        if big_count is None or count>big_count:
            big_word=word
            big_count=count
print big_word,big_count
