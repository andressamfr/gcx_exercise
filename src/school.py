class School:    
    def __init__ (self, name, email, address, telephone, director, secretary):
        self.name = name
        self.email = email
        self.address = address
        self.telephone = telephone
        self.director = director
        self.secretary = secretary
        self.teachers = []
        self.parents = []
        self.students = []