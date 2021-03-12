## Animal is-a object (yes sort of confusing) look at the extra credit:

class Animal(object):
    pass

class Dog(Animal):

    def __init__(self,name):
        ## dog has-a name
        self.name = name

class cat(Animal):
    def __init__(self,name):
        ## cat is-s animal, cat has-a named
        self.name = name

#persona is-a object
class Person(object):
    def __init__(self,name):
        ##person is a class which takes self and name as Object ??
        self.name = name

        # person has a pet of soe kind
        self.pet = None

## employee has person ( employee is-s)
class Employee(Person):
    def __init__(self, name, salary):
        #what is this strange magic?
        super(Employee,self).__init__(name)
        #(employee has a salary)
        self.salary = salary

## fish is a object
class Fish(object):
    pass
#salmon is a fish
class Salmon(Fish):
    pass

## halibut is a Fish
class Halibut(Fish):
    pass

##rover is-a dog
rover = Dog("rover")

##Satan is a cat
satan = cat("satan")

## mary is a persona
mary = Person("mary")

#mary has a pet is a Satan
mary.pet = satan

#frank isa Employee
frank = Employee("frank", 120000)

## frank has a pet
frank.pet = rover

# flipper is a Fish
FLipper = Fish()

# Crouse is a Sailmon
crouse = Salmon()

# harry is a Hailbut
harry = Halibut()
