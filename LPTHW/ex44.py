#class Parent(object):

#    def implicit(self):
#        print("Parent implicit")

#class Child(Parent):
#    pass

#dad = Parent()
#son = Child()

#dad.implicit()
#son. implicit()

#class Parent(object):

#    def override(self):
#        print("Parent override()")

#class Child(Parent):

#    def override(self):
#        print("child override()")


#dad = Parent()
#son = Child()

#dad.override()
#son.override()


#class Parent(object):

#    def alter(self):
#        print("Parent altered()")

#class Child(Parent):

#    def alter(self):
#        print("child before parent altered()")
#        super(Child,self).alter()
#        print("child after parent altered")


#dad = Parent()
#son = Child()

#dad.alter()
#son.alter()

class other:
    def override(self):
        print("other override")

    def implicit(self):
        print("other immplicite")

    def altered(self):
        print("other altered")

class child:
    def __init__(self):
        self.other = other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("chid overrides")

    def altered(self):
        print("Child before alter")
        self.other.altered()
        print("child after alter")

son = child()

son.implicit()
son.override()
son.altered()
