from src.functions import create_schools, open_director, open_secretary, open_teacher, open_student, open_parent

schools = create_schools()

# give the user the option to choose a school and return the school object
def choose_school():
    num = 0
    for school in schools:
        num += 1
        print(f'[{num}] {school.name}')
    print('Type the number of your school:')
    school_num = int(input())
    school = schools[school_num-1]
    print(f'School selected: {school.name}')
    return school


# check if the user is a director, teacher, student, parent or secretary and return the functionalities for their role
# realize the user login
def check_role():
    
    school = choose_school()
    
    print('For e-mail, check the .csv files. Use this for password: 0000')
    print('Your email: ')
    email = input()
    print('Your password: ')
    password = input()

    if password == '0000':
        if email == school.director.get_email():
            open_director(school.director)
        elif email == school.secretary.get_email():
            return open_secretary()
        else:
            for teacher in range(len(school.teachers)):
                if email == school.teachers[teacher].get_email():
                    return open_teacher()
            for student in range(len(school.students)):
                if email == school.students[student].get_email():
                    return open_student()
            for parent in range(len(school.parents)):
                if email == school.students[parent].get_email():
                    return open_parent()
            else:
                print('E-mail is incorrect! Try again.')
                return check_role()
    else:
        print('Wrong password! Try again.')
        return check_role()

check_role()