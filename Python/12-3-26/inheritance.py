

class Person:
    def __init__(self, name:str, age:int):
        print("Inside Person Constructor")
        self.name = name
        self.age=age

    def get(self):
        print("Name is:", self.name)    
        print("Age is:", self.age)    

    
class Student(Person):
    def __init__(self, name, age, sem:int, marks1:int, marks2:int):
        print("Inside Student Constructor")
        Person.__init__(self, name, age)
        self.sem=sem
        self.marks1=marks1
        self.marks2=marks2

    def get2(self):
        print("Name is:", self.name)    
        print("Age is:", self.age)    
        print("Semester:", self.sem)

    def get_avg_marks(self):
        avg = (self.marks1 + self.marks2)/2
        print(f"Average marks of {self.name} is {avg}")    

def main():
    p1 = Person("Rudra",18)
    p1.get()
    s1 = Student("rb", 18, 4, 22, 27)
    s1.get()
    s1.get_avg_marks()

if __name__ == '__main__':
    main()
    