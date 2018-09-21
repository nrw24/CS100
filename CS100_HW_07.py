'''Navado Wray
CS100 Section 004
March 19,2018
'''
#1
def twoWords(length,firstLetter):
    i= []
    word1=''
    while len(word1)!=length:
        word1= input('Enter a word please:')
        if len(word1)==length:
            i.append(word1)
            break
    while True:
        word2=input('Enter a word beginning with')
        if word2[0]==firstLetter:
            i.append(word2)
            break
    return i

print(twoWords(5,'C'))
