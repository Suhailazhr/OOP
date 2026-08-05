'''class student:
    name = "Suhail"
    subject = "Python"
    cgpa = 9

stu1 = student()
stu2 = student()

print(stu1.name , stu1.subject, stu1.cgpa)
'''


#constractor==> init = to initialise the class it is call to build a object
 
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



#Do you recheck the repo