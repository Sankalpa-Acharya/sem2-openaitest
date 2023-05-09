

empcode = 101
empname = "John"
DoJ = "01/01/2000"
Salary = 10000

import pickle

class Employee:
    def __init__(self, empcode, empname, DoJ, Salary):
        self.empcode = empcode
        self.empname = empname
        self.DoJ = DoJ
        self.Salary = Salary

    def serialize(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize(emp_str):
        return pickle.loads(emp_str)

emp = Employee(empcode, empname, DoJ, Salary)

serialized_emp = emp.serialize()

deserialized_emp = Employee.deserialize(serialized_emp)