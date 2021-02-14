#Types of variables
#    Instance variables
#        - Will be defined inside the method
#    Class variables
#        - Will be defined outside the method but inside the class
#        - Shared by all the objects of the class
#        - Can be accessed by the object and the class
#Types of methods
#    Instance method
#        - self (i.e, object) is passed as parameter to the method
#    Class method
#        - cls (i.e, class) is passed as parameter to the method
#        - Can access and modify class state.
#    Static method
#        - Needs no specific parameter.
#        - Knows nothing about the class state.

class Student:
    college_name = "vtu"        # Class variable - college_name
    def __init__(self, name, marks):
        self.name = name        # Instance variable - self.name
        self.marks = marks      # Instance variable - self.age

    def msg(self):              # Instance method
        print(self.name + " got " + self.marks, "%")

    @classmethod
    def get_per(cls, name, marks):
        return cls(name, str((int(marks)/600)*100))

    @staticmethod
    def get_age(age):
        if age<17:
            print("Belongs to abc")
        else:
            print("Belongs to xyz")

print("Object 1")
s1 = Student("suhas", "95")
print(s1);
s1.msg();

print("college_name class variable can accessed by the class as it owns it")
print(Student.college_name)
print("college_name class variable can accessed from an object also")
print(s1.college_name)

s2 = Student.get_per("suhas bagade", "555")
s2.msg();

s1.get_age(15)
