# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# added another comment

__author__ = "Prakash Khandelwal"
__date__ = "$Feb 1, 2015 2:24:10 PM$"

from nltk import *

def Tokenization(sent1):
    list1=word_tokenize(sent1)
    print list1
    i=0
    while(list1[i]!=0):
        StemmingFunc(list1[i])
        i+=1

def StemmingFunc(word1):
    wnl=WordNetLemmatizer()
    stemWord=wnl.lemmatize(word1)
    print stemWord
           
Tokenization(input("enter sent: "))

