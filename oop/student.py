class Student:
        school = "AkiraChix"
        def __init__ (self, first_name, last_name, age, country, code):
                self.first_name = first_name
                self.last_name = last_name
                self.age = age
                self.country = country
                self.code = code

                # agnes = Student(first_name="Agnes", last_name="Wangesha", country= "Kenya", age = 21, code = 79)
                # faith = Student(first_name="Faith", last_name="Mutava", country= "Kenya", age = 21, code = 27)
                # glory = Student(first_name="Glory", last_name="Wachira", country= "Kenya", age = 21, code = 2)
        def greet_student(self):
            greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}."
            return greeting

  
        def year_of_birth(self):
            return f"Hello {self.first_name}, you were born in {2024 - self.age}."
        
        # def show_full_name(first_name, last_name):
        #     full_name = f"{first_name} {last_name}"
        #     return full_name
        #     first_name="karen"
        #     last_name="philip"
        #     full_name = shoow_full_name(first_name, last_name)
        #     prrint(full_name)
        # def show_initials(first_name, last_name):
        #     initiasl = f"{k} {p}"
        #     return initiasl
        #     first_name_initial= "k"
        #     last_name_initial="p"
        #     initiasl = show_initials(first_name, last_name)
        #     print(initiasl)
        # def  check_minor(age):
        #     if age < 18:
        #         return True
        #     else:
        #         return False
        #     Student1_age = 23
        #     Student2_age = 12
        #     if check_minor(Student1_age):
        #         print("student 1 is not a minor")
        #     else:
        #         print("student is a minor")
class ClassEnrollment:
        def __init__(self, class_name, max_students):
            self.class_name = class_name
            self.max_students = max_students
            self.enrolled_students = []
        def enroll_student(self, student_name):
            if len(self.enrolled_students) < self.max_students:
                self.enrolled_students.append(student_name)
                print(f"{student_name} has been enrolled in {self.class_name}.")
            else:
                print(f"Sorry, {self.class_name} is full. Cannot enroll {student_name}.")
        def display_enrolled_students(self):
            print(f"Students enrolled in {self.class_name}:")
            for student in self.enrolled_students:
                print(student)