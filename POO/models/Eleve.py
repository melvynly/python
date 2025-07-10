class Eleve:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name


ella = Eleve("test")
ella