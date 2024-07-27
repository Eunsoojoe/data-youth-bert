# -*- coding:utf-8 -*-
#morp analysis tools
#from konlpy.tag import Mecab
#from konlpy.tag import Twitter

from konlpy.utils import pprint
from nltk.corpus import  names
import nltk
import re
import time
import csv
from konlpy.utils import concordance
from konlpy.tag import Okt
#mecab = Mecab()
#mecab = Twitter()
mecab = Okt()

from ctypes import *
import json
import string
import codecs
import json



class Sentiment():

	def data_list(wordname):	
		with open('data/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f:
			data = json.load(f)
		result = ['None','None']	
		for i in range(0, len(data)):
			if data[i]['word'] == wordname:
				result.pop()
				result.pop()
				result.append(data[i]['word_root'])
				result.append(data[i]['polarity'])	
		
		r_word = result[0]
		s_word = result[1]
		if s_word: 				
		    #print('어근 : ' + r_word)
		    #print('극성 : ' + s_word)	
		
		    return r_word, s_word



def korProcessing(korContentArray):
    tags_ko = mecab.pos(korContentArray)
    #pprint(tags_ko)
    # Define a chunk grammar, or chunking rules, then chunk
    
    '''
           AP: {<Adj.*>*}            # Adjective phrase,         NUM : {<NNG>*<NR>*<JKS>}

    '''

    grammar = """
        NP: {<N.*>*<Suffix>?<MAG>*<J.*>*<XSN>*<N.*>*}   # <MAG>* Noun phrase
        VP: {<XSV>*<V.*>*<ETM>*<EC>*<EF>*}            # Verb phrase
        ADJ: {<N.*>*<Adj.*>*<N.*>}
        SUB_NP: {<MAG>*<NN.*>*<JKS>*<NNB>}
        SUB_NP: {<NNG>*<VA>*<ETM>*<JKS>}
        """

    #parser_ko = nltk.RegexpParser("NP: {<Adjective>*<Noun>*}")
    parser_ko = nltk.RegexpParser(grammar)
    chunks_ko = parser_ko.parse(tags_ko)
    #pprint(chunks_ko)
    #pprint(parser_ko)
    #print(korContentArray)
    #pprint(chunks_ko)
    #print("print whole tree")
    print(chunks_ko.pprint()) #print subtree
    #chunks_ko.draw()

    print("\n# Print noun phrases only")
    for subtree in chunks_ko.subtrees():
        if subtree.label()=='NP':
            #print(' '.join((e[0] for e in list(subtree))))
            print(subtree.pprint())
            #print('ner: ', e.ner(korContentArray))
            #print 'subtree leaves'
            #print subtree.leaves()
        elif subtree.label()=='VP':
            #print(' '.join((e[0] for e in list(subtree))))
            print(subtree.pprint())
        elif subtree.label()=='AP':
            #print(' '.join((e[0] for e in list(subtree))))
            print(subtree.pprint())
        elif subtree.label()=='ADJ':
            #print(' '.join((e[0] for e in list(subtree))))
            print(subtree.pprint())            
        
        elif subtree.label()=='SUB_NP':
            #print(' '.join((e[0] for e in list(subtree))))
            print(subtree.pprint())
        
        
            #print(' '.join((e[0] for e in list(subtree))))
            #print(subtree.pprint())
            #print 'misc'

def korProcessingAdj(korContentArray):
    tags_ko = mecab.pos(korContentArray)
    #pprint(tags_ko)
    # Define a chunk grammar, or chunking rules, then chunk
    
    '''
           AP: {<Adj.*>*}            # Adjective phrase,         NUM : {<NNG>*<NR>*<JKS>}

    '''

    grammar = """
        VP: {<XSV>*<V.*>*<ETM>*<EC>*<EF>*}            # Verb phrase
        ADJ: {<N.*>*A<V.*>*<Adj.*>*<N.*>}
        KP: {<Ex.*>*<Ko.*>*}
        """

    #parser_ko = nltk.RegexpParser("NP: {<Adjective>*<Noun>*}")
    parser_ko = nltk.RegexpParser(grammar)
    chunks_ko = parser_ko.parse(tags_ko)
    #pprint(chunks_ko)
    #pprint(parser_ko)
    #print(korContentArray)
    #pprint(chunks_ko)
    #print("print whole tree")
    #print(chunks_ko.pprint()) #print subtree
    #chunks_ko.draw()
    word=''
    print("\n# Print noun phrases only")
    for subtree in chunks_ko.subtrees():
        if subtree.label()=='VP':
            #print(' '.join((e[0] for e in list(subtree))))
            #word = ''.join((e[0] for e in list(subtree)))
            print(subtree.pprint())
        elif subtree.label()=='ADJ':
            #print(' '.join((e[0] for e in list(subtree))))
            #word = ''.join((e[0] for e in list(subtree)))
            print(subtree.pprint())
        elif subtree.label()=='KP':
            #print(' '.join((e[0] for e in list(subtree))))
            #word = ''.join((e[0] for e in list(subtree)))
            print(subtree.pprint())    
        #print(ksl.data_list(word))                  

    
    #print str(unicode(chunks_ko))
    #print 'display the chunk tree'
    #chunks_ko.draw()
################################

def korProcessingNP(korContentArray):
    tags_ko = mecab.pos(korContentArray)
    #pprint(tags_ko)
    # Define a chunk grammar, or chunking rules, then chunk
    

    grammar = """
        NP: {<N.*>*<N.*>*}   # Noun phrase
         """

    #parser_ko = nltk.RegexpParser("NP: {<Adjective>*<Noun>*}")
    parser_ko = nltk.RegexpParser(grammar)
    chunks_ko = parser_ko.parse(tags_ko)
    #pprint(chunks_ko)
    #pprint(parser_ko)
    #print(korContentArray)
    #pprint(chunks_ko)
    #print("print whole tree")
    #print(chunks_ko.pprint()) #print subtree
    #chunks_ko.draw()

    print("\n# Print noun phrases only")
    a =[]
    word=''
    for subtree in chunks_ko.subtrees():
        if subtree.label()=='NP':
            print(''.join((e[0] for e in list(subtree))))
            #word = ''.join((e[0] for e in list(subtree))) 
            #print(subtree.pprint())
        a =[]
        #print(subtree)
        #print(ksl.data_list(word))
        
########################################
#main                  

rawFilename = 'twitter.txt'

rawT = 'cbs.txt'
senti = Sentiment

f = open(rawT, "r")
for line in f.readlines():
    if line.split() != 0:
        #print(line)
        #korProcessing(line) #using the code
        tok = mecab.pos(line) #okt 
        for read in tok:
            #print(read[0])
            rWord, sWord = senti.data_list(read[0])
            
            if sWord != 'None':
                #print(read[0])
                print('pplality => ', rWord, sWord)
        
        #input()

    #time.sleep(3)
f.close()


'''
f = open(rawT, "r")
for line in f.readlines():
    if line.split() != 0:
        #print(line)
        tags_ko = mecab.pos(line)
        pprint(tags_ko)
f.close()
'''