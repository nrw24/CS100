'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#2
def file_stats(in_file):
    infile = open(in_file)
    content = infile.read()
    wordList = content.split()
    print(len(wordList))
    lineList = in_file.readlines()
    print(len(lineList))
    num_char = infile.read()
    infile.close()
    print(len(num_char))
