from src.person import Person

class Student(Person):
    def __init__(self, name, email, address, school, disciplines, parents):
        super().__init__(name, email, address, school)
        self.disciplines = disciplines
        self.parents = parents
    
    def get_parents(self):
        return self.parents
    
    def show_pending_exams(self):
        for discipline in self.disciplines:
            for exam in discipline.exams:
                if exam['answers'].keys() != self.name:
                    return exam
                    
    def answer_exam(self, choice):
        # exam = get_exam(choice)
        print('Exam {exam} selected:')