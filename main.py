class Roditeli1:
    def __init__(self):
        self.attr1 = "Atribut 1 iz Roditeli1"


class Roditeli2:
    def __init__(self):
        self.attr2 = "Atribut 2 iz Roditeli2"


class Child(Roditeli1, Roditeli2):
    def __init__(self):
        Roditeli1.__init__(self)
        Roditeli2.__init__(self)
        self.attr3 = "Atribut 3 iz child"

child = Child()
print(child.attr1)
print(child.attr2)
print(child.attr3)
