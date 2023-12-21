class Employee:

    number_of_employees = 0

    def __init__(self, name):
        Employee.number_of_employees += 1
        self.id = Employee.number_of_employees
        self.fname

    def get_name(self):
        return self.name, self.surname
    
    def is_excluded(self):
        return self.excluded
    
    def give_demerit(self):
        self.demerit += 1


