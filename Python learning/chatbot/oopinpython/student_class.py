# solve problems by creating object
# benifit : 1. increase reusability and decress complexicity 2. easier for debug and modify and reduce code repitation

#class : class is a blue print for creating a object and it define the properity and methods that an object will have. 
# EXAMPLE:  a CLASS called DOG might have property like breed color and METHOD like bark, run 
#### method are like task or operaton of class.
#............... medthod are function define inside a class that describe the behaviour of the object 

#creating first class 
class student:
    def __init__(self, name, age, grade):
        #attributes: student's name, age, grade
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"Name is : {self.name}, Age: {self.age}, Grade: {self.grade}"
    def is_passing(self):
        #method : checks if the student is passing 
        return self.grade >= 60

# creating student object
st1 = student("rojay", 25, 80)
st2 = student("roshan", 30, 79.5)

#accessing the student details
print(st1.get_details())
print(st2.get_details())

#checking if the student is passing or not 
print(f"Student one is passed: {st1.is_passing()}")
print(f"student two is passed: {st2.is_passing()}")