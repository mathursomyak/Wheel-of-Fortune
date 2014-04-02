__author__ = 'skmathur'
import urllib2
import sys
import json
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter

# Open the URL to get the review data
request = urllib2.Request("http://dr.homelinux.net:81/wheel/")

try:
    page = urllib2.urlopen(request)
except urllib2.URLError, e:
    if hasattr(e, 'reason'):
        print 'Failed to reach url'
        print 'Reason: ', e.reason
        sys.exit()
    elif hasattr(e, 'code'):
        if e.code == 404:
            print 'Error: ', e.code
            sys.exit()

content = page.read()
soup = BeautifulSoup(content)

phrases = []
for phrase in soup.find_all("pre"):
    phrase = (phrase.text).split("\n")
    phrase = phrase[0:len(phrase)-1] #take of spin number
    phrases.extend(phrase)

allWords = []
for phrase in phrases:
    phrase = phrase.encode('utf8')
    words = phrase.split(" ")
    allWords.extend(words)

# Takes word - makes vectorized dict
def Atomizer(word):
    VectDict = {}
    word = str(word)
    for letter in word:
        if letter in VectDict: VectDict[letter] += 1
        else: VectDict[letter] = 1
    return VectDict
#print Atomizer('apple')

Frequency = []
for word in allWords:
    atomizedWord = Atomizer(word=word)
    Frequency.append(atomizedWord)

def GetProb(letter, frequency_list):
    dependentProb = {}
    for word in frequency_list:
        if letter in word:
            for eligLetter in word:
                if eligLetter in dependentProb: dependentProb[eligLetter] += word[eligLetter]
                else: dependentProb[eligLetter] = word[eligLetter]
    #d = OrderedDict(sorted(dependentProb.items()), key=itemgetter(1))
    return dependentProb

print GetProb('q',Frequency)







