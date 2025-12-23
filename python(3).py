#objek oriented programing (oop)
class dog:
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking"

dog1 = dog("Buddy", 3)
dog2 = dog("Molly", 5)

print(f"{dog1.name} is {dog1.age} years old.")
print(f"{dog2.name} is {dog2.age} years old.")
print(dog1.__dir__()) #untuk memunculkan semuanya

class dog:
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking"
    def mark(self):
        return f"{self.name} is {self.age} years old"

dog1 = dog("Buddy", 3)
dog2 = dog("Molly", 5)

print(dog1.mark())
print(dog2.mark())

class dog:
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} is barking"
    def mark(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,kata):
        self.katakata= kata
        return f"{self.name} says {self.katakata}"

dog1 = dog("Buddy", 3)
dog2 = dog("Molly", 5)

print(dog1.speak("Hello"))
print(dog2.speak("Hi"))

class dog:
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    #ini adlaah output dari perintak objek
    def __str__(self):
        return f"{self.name} is {self.age} years old. Ini adalah isinya object kalau diprint"
    
    def bark(self):
        return f"{self.name} is barking"
    def mark(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,kata):
        self.katakata= kata
        return f"{self.name} says {self.katakata} and {self.species}"

#membuat class child dibawah class parents
class cat(dog):
    pass

dog1 = dog("Buddy", 3)
dog2 = dog("Molly", 5)
cat1 = cat("Kitty", 4)

print(dog1)
print(cat1)

class dog:
    species = "Canis familiaris"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    #ini adlaah output dari perintak objek
    def __str__(self):
        return f"{self.name} is {self.age} years old. Ini adalah isinya object kalau diprint"
    
    def bark(self):
        return f"{self.name} is barking"
    def mark(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

#membuat class child dibawah class parents
class cat(dog):
    pass

class bulldog(dog):
    def speak(self, sound="grf"):
        return super()

dog1 = dog("Buddy", 3)
dog2 = dog("Molly", 5)
cat1 = cat("Kitty", 4)
bulldog1 = bulldog("Jim", 6)

print(dog1)
print(cat1)
print(bulldog1.speak())

