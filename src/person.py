class Person:

    def __init__ (self, name, email, address, school):
        self.name = name
        self.__email = email
        self.__address = address
        self.school = school
    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address