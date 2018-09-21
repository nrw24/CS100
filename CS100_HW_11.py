class Dog:
    '''This is a self and he does tricks'''
    species='canis familiaris'
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed
        self.tricks=[]
    def teach(self, newtrick):
        self.tricks.append(newtrick)
        print(self + 'knows', newtrick)
    def knows(self, known):
        if known in self.tricks:
            print(self.name, 'knows', known)
            return True
        else:
            print(self.name, 'does not know', known)
            return False




