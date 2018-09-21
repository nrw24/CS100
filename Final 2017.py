def isPrefix(a, b):
 prefix = ''
 index = 0
 for letter in b:
     if index >= len(a):
         return a
     elif a[index] != b[index]:
         return prefix
     else:
         prefix += b
         index += 1
 return prefix
word0 = 'asp'
word1 = 'asparagus'
print(isPrefix(word0, word1))
