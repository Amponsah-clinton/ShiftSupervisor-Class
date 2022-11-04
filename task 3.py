# parent class Tertiary
class Employee:
    def __init__(self, name, worker_id): 
        self.name = name
        self.worker_id = worker_id

# Student subclass inheriting features of Tertiary
class Shiftsupervisor(Employee):
    def __init__(self, name, worker_id , salary, bonus): 
        super().__init__( name, worker_id)
        self.salary = salary
        self.bonus = bonus
        
# displaying details of student
    def details(self):
        print("---------  HELLO ", self.name ,", here are your details.  ---------")
        print("You are :", self.name)
        print("Workers ID is :", self.worker_id)
        print("Monthly Salary is :", self.salary)
        print("Annual Bonus is :", self.bonus)

# Accepting users input
name = input("Enter your name: ")
workers_ID = int(input("Enter your workers ID: "))
salary = float(input("Enter your salary: "))
bonus = float(input("Enter your Bonus earned : "))

       
# passing users input to Shiftsupervisor and to Shiftsupervisor1        
Shiftsupervisor1 = Shiftsupervisor(name,workers_ID,salary,bonus) 

# printing workers details
print(Shiftsupervisor1.details()) 
