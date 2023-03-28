class Person:
  def __init__(self, student, pre, mid, fin):
    self.__student = student
    self.__pre = pre
    self.__mid = mid
    self.__fin = fin

  def grades(self):
    return (self.__pre + self.__mid + self.__fin) / 3

  def display(self):
    print(f"This is {self.__student}\n")
    print(f"Prelim Grade: {self.__pre}\n")
    print(f"Midterm Grade: {self.__mid}\n")
    print(f"Final Grade: {self.__fin}\n")
    print(f"Average: {round(self.grades(),2)}\n")

class Student_1(Person):
  pass
class Student_2(Person):
  pass
class Student_3(Person):
  pass

student1 = Student_1("Student 1", 85, 82, 84)
student1.display()

student2 = Student_2("Student 2", 81, 86, 89)
student2.display()

student3 = Student_3("Student 3", 85, 85, 94)
student3.display()












