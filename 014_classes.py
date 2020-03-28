class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):  # constructor
        self.name = name    # instance variable unique to each instance


# when used self, we create variable for each instance else a class variable
def __init__(self, name):
    self.name = name
    self.tricks = []    # creates a new empty list for each dog

def add_trick(self, trick):
    self.tricks.append(trick)



class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    __update = None   # private 

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# Inheritance

# class DerivedClassName(BaseClassName):
# 	pass

#multiple inheritance
# class DerivedClassName(Base1, Base2, Base3):
