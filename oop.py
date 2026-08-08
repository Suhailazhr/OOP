'''class student:
    name = "Suhail"
    subject = "Python"
    cgpa = 9

stu1 = student()
stu2 = student()

print(stu1.name , stu1.subject, stu1.cgpa)
'''


#constractor==> init = to initialise the class it is call to build a object
'''
class student:
    def __init__(self , name, cgpa):
        self.name = name
        self.cgpa = cgpa
        

stu1 = student("suhail" ,98)
stu2 = student("Waseem" ,95)
stu3 = student("Naseem" ,99)
stu4 = student("Umar" ,89)

print(stu1.name , stu1.cgpa)
print(stu2.name , stu2.cgpa)
print(stu3.name , stu3.cgpa)
print(stu4.name , stu4.cgpa)


'''
'''
class student:
    college_name = "A B C" #class attributes
    PI = 3.1

    def __init__(self): #default construtor
        print("Obj is being counstructor..")

#constructor == has two ==> default and parameterized

    def __init__(self,name,cgpa): #parameterized constructor
        self.name = name  #instance attributes
        self.cgpa = cgpa
        self.PI = 3.14

    def get_cgpa(self):
        return self.cgpa

stu1 = student("Suhail" , 9.0)



#stu1.get_cgpa()
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

print(stu1.name) #call instance attribure

print(student.college_name) #call class attribute

print(stu1.PI) #high priority is that take the value from instance attribute sa

print(student.PI) #but when we call the class attribute take the value from class attribute

'''
'''
class laptop:
    storage_type = "Ssd"

    def __init__(self , RAM , Storage):
        self.RAM = RAM
        self.Storage = Storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")

    def get_info(self): #instance Method 
        print(f"Latop has {self.RAM} & {self.Storage} {self.storage_type}")

    @staticmethod
    def cal_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"Discount Price = {final_price}")
        
l1 = laptop("16RAM","512GB")

l1.get_info()

laptop.get_storage_type()
l1.cal_discount(40_000,11)'''

# oop are four piller 
#one is encapsulation
'''
class Bankaccount:

    def __init__(self,name,balance):
        self.name = name #public attribute
        self.__balance = balance #data mangling

        #use getter and setter
    def get_balance(self): #getter
        return self.__balance

    def set_balance(self,newBalance):
        self.__balance = newBalance  

acc1 = Bankaccount("Suhail", 100_000)
acc1.set_balance(200_000)
print(acc1.name,acc1._Bankaccount__balance)'''

#second is inheritance
'''
class Employe:
        start_time = "10AM"
        end_time = "6PM"
    
class Adminstaff(Employe):
        def __init__(self,role):
            self.role = role

class Accountant(Adminstaff):
        def __init__(self, salary,role):
            super().__init__(role)
            self.salary = salary


acc1 = Accountant(25_000, "CA")

print(acc1.role,acc1.salary, acc1.start_time,acc1.end_time)'''

class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)
        Student.__init__(self,gpa)
        self.name = name

t1 = TA(25_000, 9.0, "Suhail")

print(t1.name,t1.salary,t1.gpa)