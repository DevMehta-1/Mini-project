from connect import myconnect
from val import *
from PermanentEmployee import *
class Employee:
      
      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""

      def __init__(self):
            self._empname = input("enter name: ")
            self._empemail=input("enter email: ")
            while valemail(self._empemail):
                self._empemail=input("Enter email again:")
            self._empmob=input("enter mobile no: ")
            while valmobile(self._empmob):
                self._empmob=input("Enter mobile no again:")
            self._emptype = input("enter type: ")
            self._empexp = int(input("enter experience"))
            self._empsalary = self.getsalary()
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("Invalid Employee. Please enter only 'p' or 'P'")
                  
      @staticmethod
      def addnote():
          f=open('notes.txt','a')
          n=input("Enter note:")
          f.write(n)
          print("Note added")
                  
print("1. Add Emp")
print("2. Display Emp")
print("3. Add Notes")
choice = int(input("Enter your Choice:"))
if choice == 1:
      c = Employee()
      obj = myconnect()
      obj.savetodb(c._empname,c._empemail,c._empmob,c._emptype,c._empexp,c._empsalary)
elif choice==2:
      obj = myconnect()
      obj.display()
elif choice==3:
      Employee.addnote()
else:
      print("invalid choice")
      
