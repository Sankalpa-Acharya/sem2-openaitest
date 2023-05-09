

import pickle

class Employee:
   def __init__(self, empcode, empname, DateofJoining, Salary):
      self.empcode = empcode
      self.empname = empname
      self.DateofJoining = DateofJoining
      self.Salary = Salary

# Serialize the object data

def serialize(employee):
   try:
      with open("employee.txt", "wb") as fh:
         pickle.dump(employee, fh)
         print("The data is serialized")
   except (FileNotFoundError, pickle.PicklingError) as error:
      print(error)

# Deserialize the object data

def deserialize():
   try:
      with open("employee.txt", "rb") as fh:
         employee = pickle.load(fh)
      return employee
   except (FileNotFoundError, pickle.UnpicklingError) as error:
      print(error)