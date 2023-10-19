import random
from src.discipline import Discipline
from src.school import School
from src.secretary import Secretary
from src.director import Director
from src.teacher import Teacher
from src.student import Student
from src.parent import Parent
import pandas as pd

# read the sample data
directors = pd.read_csv('./tables/directors.csv').to_dict('index')
disciplines = pd.read_csv('./tables/disciplines.csv').to_dict('index')
parents = pd.read_csv('./tables/parents.csv').to_dict('index')
schools = pd.read_csv('./tables/schools.csv').to_dict('index')
secretaries = pd.read_csv('./tables/secretaries.csv').to_dict('index')
students = pd.read_csv('./tables/students.csv').to_dict('index')
teachers = pd.read_csv('./tables/teachers.csv').to_dict('index')

# load the discipline data to the object Discipline
def create_discipline():
    disciplines_list = []
    for discipline in disciplines:
        name = disciplines[discipline]['name']
        classes = disciplines[discipline]['classes'].split(';')
        importance = disciplines[discipline]['importance']
        disciplines_list.append(Discipline(name, classes, importance))
    return disciplines_list

# load the director data to the object Director
def create_directors(disciplines_list):
    directors_list = []
    for director in directors:
        name = directors[director]['name'] + " " + directors[director]['surname']
        email = directors[director]['email']
        address = directors[director]['street'] + " " + directors[director]['city']
        school = directors[director]['school']
        directors_list.append(Director(name, email, address, school, disciplines_list))
    return directors_list

# load the secretary data to the object Secretary
def create_secretaries():
    secretaries_list = []
    for secretary in secretaries:
        name = secretaries[secretary]['name'] + " " + secretaries[secretary]['surname']
        email = secretaries[secretary]['email']
        address = secretaries[secretary]['street'] + " " + secretaries[secretary]['city']
        school = secretaries[secretary]['school']
        secretaries_list.append(Secretary(name, email, address, school))
    return secretaries_list

# load the teacher data to the object Teacher
def create_teachers(disciplines_list):
    teachers_list = []
    for teacher in teachers:
        name = teachers[teacher]['name'] + " " + teachers[teacher]['surname']
        email = teachers[teacher]['email']
        address = teachers[teacher]['street'] + " " + teachers[teacher]['city']
        school = teachers[teacher]['school']
        teacher_disc = teachers[teacher]['disciplines'].split(';')
        teacher_disc_classes = add_teacher_classes(teacher_disc, disciplines_list)
        teachers_list.append(Teacher(name, email, address, school, teacher_disc_classes))
    return teachers_list

# add the teachers to a school
def add_teachers(schools_list, disciplines_list):
    teachers_list = create_teachers(disciplines_list)
    teachers_school = []
    for school in schools_list:
        for teacher in teachers_list:
                if school.name == teacher.school:
                    teachers_school.append(teacher)
                    school.teachers = teachers_school

# add discipline classes to teacher's discipline
def add_teacher_classes(teacher_disc, disciplines_list):

    teacher_classes = {}

    for discipline_name in teacher_disc:
        for discipline in disciplines_list:
            if discipline_name == discipline.name:
                teacher_classes[discipline.name] = discipline.classes
    return teacher_classes

# load the parent data to the object Parent
def create_parents(students_list):
    parents_list = []
    for parent in parents:
        name = parents[parent]['name'] + " " + parents[parent]['surname']
        email = parents[parent]['email']
        address = parents[parent]['street'] + " " + parents[parent]['city']
        school = parents[parent]['school']
        for student in students_list:
            for parent_ in student.parents:
                if parent_ == name:
                    parent_students = student
        parents_list.append(Parent(name, email, address, school, parent_students))
    return parents_list

# choose randomly discipline classes to the student
def choose_disc_classes(disciplines_list):
    
    student_classes = {}
    optional = {}

    for discipline in disciplines_list:
        if discipline.importance == 'mandatory':
            mandatory = discipline
            class_choice = random.choice(mandatory.classes)
            student_classes[mandatory.name] = class_choice
        else:
            optional[discipline] = discipline

    opt_choice = random.choice(list(optional))
    class_choice = random.choice(opt_choice.classes)
    student_classes[opt_choice.name] = class_choice

    return student_classes

# load the student data to the object Student
def create_students(disciplines_list):
    students_list = []
    for student in students:
        name = students[student]['name'] + " " + students[student]['surname']
        email = students[student]['email']
        address = students[student]['street'] + " " + students[student]['city']
        school = students[student]['school']
        student_parents = students[student]['parents'].split(';')
        disc_classes = choose_disc_classes(disciplines_list)
        students_list.append(Student(name, email, address, school, disc_classes, student_parents))
    create_parents(students_list)
    return students_list

# add students to a school
def add_students(schools_list, disciplines_list):
    students_list = create_students(disciplines_list)
    students_school = []
    for school in schools_list:
        for student in students_list:
                if school.name == student.school:
                    students_school.append(student)
                    school.students = students_school

# load the school data and objects to the object School
def create_schools():
    schools_list = []
    disciplines_list = create_discipline()
    directors_list = create_directors(disciplines_list)
    secretaries_list = create_secretaries()

    for school in schools:
        name = schools[school]['name']
        email = schools[school]['email']
        address = schools[school]['street'] + " " + schools[school]['city']
        director_name = schools[school]['director']
        secretary_name = schools[school]['secretary']
        telephone = schools[school]['telephone']
        for director in directors_list:
            if director_name == director.name:
                school_director = director
        for secretary in secretaries_list:
            if secretary_name == secretary.name:
                school_secretary = secretary
        schools_list.append(School(name, email, address, telephone, school_director, school_secretary))
        
    add_teachers(schools_list, disciplines_list)
    add_students(schools_list, disciplines_list)
        
    return schools_list

# show director's functionalities
def open_director(director):
    finish = 'no'
    while finish == 'no':
        print('**Menu**')
        print('[1] Create exam\n[2] Grade exams')
        choice = int(input())

        print('List of disciplines:')
        director.show_disciplines_name()

        print('Type the name of a discipline')
        disc_choice = input()
        discipline = director.get_discipline(disc_choice)

        if choice == 1:
            director.create_exam(disc_choice)
        else:
            print('Select an exam: ')
            discipline.show_exams_name()
            exam_choice = input()
            exam = discipline.get_exam(exam_choice)
            director.grade_exam(exam)
        print('Logout?')
        finish = input()
        
# show secretary's functionalities
def open_secretary():
    return None

# show teacher's functionalities
def open_teacher():
    return None

# show student's functionalities
def open_student(student):
    finish = 'no'
    while finish == 'no':
        print('**Menu**')
        print('[1] Answer exam\n[2] See grades')
        choice = int(input())

        if choice == 1:
            print('Exams pending:')
            student.show_pending_exams()

            print('Type the name of the exam to perform:')
            disc_choice = input()
            exam = student.get_discipline(disc_choice)

            student.answer_exam(exam)
        else:
            student.show_grades()
        print('Logout?')
        finish = input()

# show parents's functionalities
def open_parent():
    return None