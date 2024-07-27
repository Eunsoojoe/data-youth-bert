from konlpy.tag import Kkma
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.chunk.regexp import RegexpParser
import pandas as pd

file_name = ("Output\comments_union\최종_웹사이트(emoji,url 제거).xlsx")
df = pd.read_excel(file_name) 
sentence = []


rules = RegexpParser("""
        NP: {<N.*>*<Suffix>?<MAG>*<J.*>*<XSN>*<N.*>*}   # <MAG>* Noun phrase
        VP: {<XSV>*<V.*>*<ETM>*<EC>*<EF>*}            # Verb phrase
        ADJ: {<N.*>*<Adj.*>*<N.*>}
        SUB_NP: {<MAG>*<NN.*>*<JKS>*<NNB>}
        SUB_NP: {<NNG>*<VA>*<ETM>*<JKS>}
        """)


for text in df['command']:
    tagged = Kkma().pos(text)
    parseTree = rules.parse(tagged).draw()
    parseTree
    
    for substree in parseTree.subtress():
        if substree.label() == "NP":
            print(substree)





    