'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#3
def shareALetter(wordList):
    d={}
    for word in wordList:
        for letter in word:
            if letter not in d:
                d[word]=[word]
            if letter in wordList:
                d.update(word)
    return d
horton= ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareALetter(horton))
