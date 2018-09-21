'''Navado Wray
CS100 Section 004 S18
March 24,2018'''
#3
from string import punctuation as p
def repeat_words(in_file, out_file):
    f=open(in_file, 'r')
    w=open(out_file, 'w')
    lines=f.readlines()
    for line in lines:
        for  word in line:
            if line.count(word)>1:
                word.strip(p)
                word.lower()
                w.write(word)
    w.close()
    f.close()

