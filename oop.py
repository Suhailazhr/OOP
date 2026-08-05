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

class student:
    college_name = "A B C" #class attributes
    PI = 3.1

    '''def __init__(self): #default construtor
        print("Obj is being counstructor..")
'''
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




