class Person:
    def __init__ (self, fname, lname):
        self.fname = fname
        self.lname = lname
        

p1 = Person('Himanshu', 'Singla')
p2 = Person("Tushar", "Kumar")

print(p1.fname)
print(p2.lname)