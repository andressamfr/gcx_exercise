from src.person import Person

class Parent(Person):
    def __init__(self, name, email, address, school, students):
        super().__init__(name, email, address, school)
        self.students = students

    def get_student(self):
        return self.students