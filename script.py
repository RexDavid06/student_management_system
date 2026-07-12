
class Student:
    'static attribute'
    total_students = 0
    def __init__(self, name, age, course):
        self.name = name 
        self.age = age
        self.course = course
        Student.total_students += 1

        with open('students.txt', 'a') as af:
            af.write(f"{self.name}|{self.age}|{self.course}\n")
    
    @staticmethod
    def view_students():
        with open('students.txt', 'r') as rf:
            rf_contents = rf.read()
            print(rf_contents)

    @staticmethod
    def search_student(student):
        pass


    @staticmethod
    def delete_student(student):
        del student


  
   

student1 = Student('Angel', 19, 'Biochemistry')
student2 = Student('Gabriel', 24, 'Mechanical Engineering')
student3 = Student('Luke', 28, 'Medicine and Surgery')
student4 = Student('unkmown', 28, 'Pharmacy')

print(f"Total Students: {Student.total_students}")
Student.view_students()
Student.delete_student(student4)
Student.view_students()
