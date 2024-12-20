#create a class
class student:
    #assign a variable grade
    grade=10
    #assaign variable name
    name="Ketra"
    #create a function
    def introduction(self):
    #print a statement using the variable
        print("Hi, i am a student ")
    #function to print to name and grade
    def details(self):
        print("My name is ",self.name,"I am in grade ",self.grade)
#create an object OBJECTS ARE NOT CREATED INSIDE A CLASS
ob= student()
ob.introduction()
ob.details()