class student:
    def __init__(self,name,age,cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Cgpa : {self.cgpa}")

    def update_cgpa(self,new_cgpa):
        self.cgpa = new_cgpa
        print("CGPA Update Successfully..")

stu1 = student("SUHAIL", 21, 9.5)

stu1.display_info()
print("\n")

stu1.update_cgpa(9.1)

stu1.display_info()