class Enroll :
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age


enroll = Enroll (1,"yibeltal", 21)
print(f"his name is {enroll.name.upper()} and he is {enroll.age} years old")

class Person :
    def __init__(self,first, last):
        self.first = first
        self.last = last

    def name(self):
        return self.first + " " + self.last
person = Person ("yibeltal", "marie")
print(person.name())

