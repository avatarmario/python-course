class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.courses = []
        self.student_id = student_id

        def greet(self):
            print(f"Hello, my name is {self.name}, I am {self.age} years old, and my student ID is {self.student_id}.")

student = Student("Mario", 20, "S12345")
student.greet()  # Output: Hello, my name is Mario, I am 20 years old, and my student ID is S12345.
