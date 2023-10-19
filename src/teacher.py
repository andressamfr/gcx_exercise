from src.director import Director

class Teacher(Director):
    def __init__(self, name, email, address, school, disciplines):
        super().__init__(name, email, address, school, disciplines)

    