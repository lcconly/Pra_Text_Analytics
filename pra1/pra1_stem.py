#####differernce betwwen poterstemmer and Lemmatizer
import re, collections, os
import nltk
from nltk.stem import PorterStemmer
########get the location of current file
__location__=os.path.realpath(
        os.path.join(os.getcwd(),os.path.dirname(__file__))
    )
print(__location__)
##########original
file_name=os.path.join(__location__,"text_1.txt")
file=open(file_name)
txt=file.read()
tokens=nltk.word_tokenize(txt)
words=[w.lower() for w in tokens]
print(words)
input()
#########porterStemmer
#splittxt=txt.split(" ")
stemmer=PorterStemmer()
#stemmertxt=[stemmer.stem(wd). lower() for wd in splittxt]
stemmertxt=[stemmer.stem(wd).lower for wd in words]
input()
#########Lemmatizer
wn=nltk.WordNetLemmatizer()
lemmTxt=[wn.lemmatize(wd).lower() for wd in words]
#print different
for index in range(len(words)):
    if stemmertxt[index]!=lemmTxt[index]:
        print(stemmertxt[index]+"   "+lemmTxt[index]+"\n")
