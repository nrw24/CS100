'''class State:
    'Universities in New Jersey'
    def __init__(self,name):
        self.name=name
        self.universities=[]
    def addUniversity(self,university):
        self.universities.append(university)
    def is_home_of(self, university):
        if university in self.universities:
            return True
        else:
            return False
import state
nj=state.State('New Jersey')
nj.addUniversity('NJIT')
nj.addUniversity('Princeton')
print(nj.is_home_of('MIT'))'''
'''def lineStats(inn,out):
    inF=open(inn)
    outF=open(out, 'w')
    for line in inF:
        index=0
        if line.count(
        words=line.lower().split()
        unique=[]
        for word in words:
            if word in unique:
                continue
            if line.count(word)>1:
                lst.append(word)
        print('words: {}'.format(str(len(unique))))'''
def vowelCount(s):
    vowels='aeiou'
    x=s.lower().split()
    count=0
    for word in x:
        for letter in word:
            if letter in vowels:
                count+=1

    return count
print(vowelCount('Amen'))
def vowelFrequency(t):
    d={}
    words=t.lower().split()
    for word in words:
        count=vowelCount(word)
        if count not in d:
            d[count]=[word]
        else:
            if word not in d[count]:
                d[count].append(word)
    return d
        
            
text= "Where hunger is ugly where souls are forgotten"
print(vowelFrequency(text))
