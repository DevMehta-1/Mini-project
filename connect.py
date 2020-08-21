import sqlite3
class myconnect:
      
      def __init__(self):
            conn=sqlite3.connect('emp.db')
            conn.execute('''create table if not exists Employee (id integer primary key autoincrement,name text,email text,mobile_no integer,employee_type text,experience integer,salary integer) ''')
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            conn=sqlite3.connect('emp.db')
            conn.execute('insert into Employee values(NULL,?,?,?,?,?,?)',(ename,eemail,emob,etype,eexp,esalary))
            conn.commit()
            conn.close()

      def display(self):
             id=int(input("Enter the emp id:"))
             conn=sqlite3.connect('emp.db')
             data=conn.execute('select * from Employee where id = ?',(id,))
             f=0
             for row in data:
                 f=1
                 print("==================================================")
                 print("Name:",row[1])
                 print("Email:",row[2])
                 print("Mobile no:",row[3])
                 print("Employee type:",row[4])
                 print("Experience:",row[5])
                 print("Salary:",row[6])
                 print("==================================================")
             if(f==0):
                print("Enter valid ID")
             conn.close()