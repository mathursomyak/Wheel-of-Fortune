__author__ = 'skmathur'
import urllib2
import sys
import json
from bs4 import BeautifulSoup
from collections import OrderedDict
from operator import itemgetter

def pull_page(url,return_words = True):
    # Open the URL to get the review data
    request = urllib2.Request(url)

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

    if return_words: return allWords
    else: return phrases

def pull_all_pages():
    webpageExtensions = ['','w2012.html','w2011.html','w2010.html','w2009.html','w2008.html','w2007.html','w2006.html','w2005.html','w2004.html','w2003.html']
    allWords = []
    for ext in webpageExtensions:
        url = "http://dr.homelinux.net:81/wheel/"+ext
        words = pull_page(url)
        allWords.extend(words)
    return allWords





