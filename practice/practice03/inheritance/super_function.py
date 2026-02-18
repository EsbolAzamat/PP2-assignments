class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

    def info(self):
        print(self.name, "studies at", self.university)

s = Student("Ali", "KBTU")
s.info()
