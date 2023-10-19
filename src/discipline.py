class Discipline:
    
    def __init__ (self, name, classes, importance):
        self.name = name
        self.classes = classes
        self.importance = importance
        self.exams = {}

    def get_exam(self, choice):
        for exam in self.exams:
            if choice == exam:
                return self.exams[exam]
            
    def show_exams_name(self):
        for exam in self.exams:
            print(exam)