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

def oddOrEven():
    num = int(input("Enter a number to check if a number is odd or even: "))
    if(num % 2 == 0):
        print(f"{num} The number is Even")
    else:
        print(f"{num} The number is Odd")            

def main():
    greet("eg", age)
    # Ask()
    oddOrEven()


if __name__ == "__main__":
    main()