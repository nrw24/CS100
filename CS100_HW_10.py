'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#1
def initialLetterCount(wordList):
    d={}
    for word in wordList:
        if word not in d:
            d[word]=0
        else:
            d[word]+=1
    return d
        
lst=['i','s','as','i','as','s','p','l','p']
print(initialLetterCount(lst))
        
