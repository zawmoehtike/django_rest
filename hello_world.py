
# age = 27
# name = 'Zaw'

# if age == 26:
#     print('Age is 26')
# else:
#     print('Age is not 26')

# print(name,age,name)

# while age > 1:
#     age -= 1
#     print('Age minus 1:', age)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

class SonOfDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age)
        self._weight = weight # single underscore is for encapsulation

    def barkLoudly(self):
        print("Woof! x 2")

    def getWeight(self):
        return self._weight

# purpleDog = Dog("Purple Dog", 5)
# purpleDog.bark()
# print(purpleDog.name)

sonOfPurpleDog = SonOfDog(name = "Green Dog", age = 2, weight = None) # None is null
sonOfPurpleDog.bark()
sonOfPurpleDog.barkLoudly()
print(sonOfPurpleDog.getWeight())

