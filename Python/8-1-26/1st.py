# This is a sample Python script.
age = 17

def greet(name, age):
    print("Hi " + name + " Your Age is " + str(age))


# Determine age category
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


# Check if a number is odd or even
def oddOrEven():
    num = int(input("Enter a number to check if a number is odd or even: "))
    if(num % 2 == 0):
        print(f"{num} The number is Even")
    else:
        print(f"{num} The number is Odd")


# Check odd or even in a given range
def oddOrEvenRange():
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))

    if(lower > upper):
        print("Invalid Range! Upper range must be greater than lower range.")
        return

    for num in range(lower, upper + 1):
        if(num % 2 == 0):
            print(f"{num} The number is Even")
        else:
            print(f"{num} The number is Odd") 



# Main function to execute the script
def main():
    greet("eg", age)
    # Ask()
    oddOrEven()
    oddOrEvenRange()

# Execute main function
if __name__ == "__main__":
    main()