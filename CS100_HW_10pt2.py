'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#2
hamlet = ["To", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
antony = ["Friends", "Romans", "countrymen", "lend", "me", "your", "ears"]
macbeth = ["Tomorrow", "and", "tomorrow", "and", "tomorrow"]
def initialLetters(wordList):
    d={}
    for word in wordList:
            if word[0] not in d:
                d[word[0]]=[word]
    return d
horton= ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))
print('\n----------Testing 2-----------')
for testCase in (hamlet, antony, macbeth):
    print("Test Case:", testCase)
    print("Dictionary:", initialLetters(testCase))
    print()
