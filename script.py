from typing import List

class Student:
    def __init__(self, name: str, age: int, course: str) -> None:
        self.name = name
        self.age = age
        self.course = course

    
    def save(self) -> None:
        try:
            with open('students.txt', 'a') as wf:
                wf.write(f"{self.name}|{self.age}|{self.course}\n")
        except FileNotFoundError as e:
            print(e)
        
    @classmethod
    def view_students(cls) -> None:
        try:
            with open('students.txt', 'r') as rf:
                rf_contents = rf.read()
                print(rf_contents)
        except FileNotFoundError as e:
            print(e)
    
    @classmethod
    def search_student(cls, student_name: str) -> None:
        found = False
        try:
            with open('students.txt', 'r') as rf:
                for line in rf:
                    name, age, course = line.strip().split('|')
                    if student_name == name:
                        print(line)
                        found = True
        except FileNotFoundError as e:
            print(e)
        else:
            if not found:
                print(f"{student_name} isn't in file")
        
    
    @classmethod
    def delete_student(cls, student_name: str) -> None:
        found = False
        remaining_students:List[str] = []
        try:
            with open('students.txt', 'r') as rf:
                for line in rf:
                    name, age, course = line.strip().split('|')
                    if student_name == name:
                        found = True
                        continue
                    remaining_students.append(line)
                with open('students.txt', 'w') as wf:
                    wf.writelines(remaining_students)
        except FileNotFoundError as e:
            print(e)
        else:
            if not found:
                print(f"{student_name} isn't in file")
        

    @classmethod
    def menu(cls):
        try:
            while True:
                options = int(input('Choose from the menu\n1) Add Student\n2) View Student\n3) Search Student\n4) Delete Student\n5) Exit\n'))
                if options == 5:
                    break
                elif options == 1:
                    name = str(input('Name: '))
                    age = int(input('Age: '))
                    course = str(input('Course: '))
                    student = Student(name, age, course)
                    student.save()
                elif options == 2:
                    Student.view_students()
                elif options == 3:
                    student_name = str(input("enter student's name: "))
                    Student.search_student(student_name=student_name)
                elif options == 4:
                    student_name = str(input("enter student's name: "))
                    Student.delete_student(student_name=student_name)
                else:
                    print('Choose from 1-5')
        except Exception as e:
            print(e)

Student.menu()