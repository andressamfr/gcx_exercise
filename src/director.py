import csv
from src.person import Person

class Director(Person):
    def __init__(self, name, email, address, school, disciplines):
        super().__init__(name, email, address, school)
        self.disciplines = disciplines

    def show_disciplines_name(self):
        for discipline in self.disciplines:
            print(discipline.name)

    def get_discipline(self, name):
        for discipline in self.disciplines:
            if discipline.name == name:
                return discipline
            
    def create_exam(self, discipline):
        discipline = self.get_discipline(discipline)
        exam = {}
        questions = []
        answers = {}
        more_questions = 'yes'
        counter = 1

        print('Add a name abbreviation for the exam:')
        exam_name = input()

        while more_questions == 'yes':
            print(f'Exam question {counter}:')
            question = input()
            # print(f'Answer {counter}:')
            # answer = input()
            questions.append(question)
            print('Add another question?')
            more_questions = input().lower()
            counter += 1
        discipline.exams[exam_name] = exam
        discipline.exams[exam_name]['questions'] = questions
        discipline.exams[exam_name]['answers'] = answers

        # with open('./tables/exams.csv', 'w') as file: 
        #     exams_file = csv.DictWriter(file, fieldnames = fields)
            
    
    def grade_exam(self, exam):
        for student_answers in exam['answers']:
            student = student_answers.key()
            print(f'{student_answers} \n Give points:')
            points += input()

        print(f'Grade: {points}')
        exam['answers'][student]['grade'] = points