__author__ = 'skmathur'
import collections

import PullCorpus


allWords = PullCorpus.pull_page(url= "http://dr.homelinux.net:81/wheel/")
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

def LettersInWord(letters,word):
    inWord = [i for i in letters if i in word]
    if len(inWord)==len(letters): return True
    else: return False

#print LettersInWord(['f','f'],'frog')

def GetProb(letters, frequency_list=Frequency, num_recs=None):
    if num_recs == 0: num_recs = len(letters)+1
    dependentProb = {}
    for word in frequency_list:
        if LettersInWord(letters,word):
            for eligLetter in word:
                if eligLetter in dependentProb: dependentProb[eligLetter] += word[eligLetter]
                else: dependentProb[eligLetter] = word[eligLetter]
    d = collections.Counter(dependentProb)
    return d.most_common(num_recs)

def Prettify(list_of_tups,num_to_display):
    returnString = ''
    for i in range(num_to_display):
        returnString = returnString + list_of_tups[i]+'\n'
    return returnString

print len(allWords)