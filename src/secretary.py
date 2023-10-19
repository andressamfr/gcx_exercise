from src.person import Person

class Secretary(Person):
    def __init__(self, name, email, address, school):
        super().__init__(name, email, address, school)