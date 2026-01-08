# This is a sample Python script.
age = 17

def greet(name, age):
    print("Hi " + name + " Your Age is " + str(age))

def Ask():


    age = int(input("Enter your age: "))

    if(age<0):
        print("Invalid Age")
        return

    if(age>18 and age<=60):
        print("You are Adult")
        if(age>60):
            print("You are Senior Citizen")
    elif(age < 18 and age>12):
        print("You are a Teenager")
    else:
        print("You are a Child")            

def main():
    greet("eg", age)
    Ask()


if __name__ == "__main__":
    main()