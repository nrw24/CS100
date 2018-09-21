'''1.d
2.c
3.e
4.d
5.c
6.c
7.a
8.e
9.e
10.b'''
def aSym(aString):
 words = aString.split()
 left = 0
 right = -1
 for word in words:
     if words[left] != words[right]:
         return word
     left += 1
     right -= 1
 return ""
s = 'all for one trumps one for all'
print(aSym(s))
