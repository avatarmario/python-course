class LivingBeing:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")    

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print(f"{self.name} says hello.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def speak(self):
        print(f"{self.name} says hello and my student ID is {self.student_id}.")

#Test
living_being = LivingBeing("Generic Being")
living_being.speak()  # Output: Generic Being makes a sound. 
student = Student("Mario", 20, "S12345")
student.speak()  # Output: Mario says hello and my student ID is S12345