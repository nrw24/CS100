'''Navado Wray
CS 100 Section 004
February 14, 2018 HW06'''
#1a

def hasFinalLetter(strList,letters):
    x=[]
    for string in strList:
        if string[-1] in letters:
            x.append(string)
    return x
#2a

def isDivisible(maxInt,twoInts):
    x=[]
    for number in range(1,maxInt+1):
        if number%twoInts[0]==0 and number%twoInts[1]==0:
            x.append(number)
    return x

#1b

List=['cars','junk','laugh']
list2=['table','closet','airhorn','zebra']
list3=['dog','husky','dog','cat']
letters='garesk'
letters2='ahjscbhaj'
letters3='jin'
print(hasFinalLetter(List,letters))
print(hasFinalLetter(list2,letters2))
print(hasFinalLetter(list3,letters3))

#2b

integer=5
two_numbers=(3,2)
twoInts=(1,2)
twoNums=2,4
Int=11
num=24
print(isDivisible(integer,two_numbers))
print(isDivisible(Int,twoInts))
print(isDivisible(num,twoNums))
