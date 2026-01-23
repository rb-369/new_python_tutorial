

def sep():

    
    lim = int(input("Enter the limit: "))
    if(lim < 0):
        print("Invalid limit! Limit must be non-negative.")
        return
    even_numbers = []
    odd_numbers = []    

    for n in range(0, lim+1):
        if (n%2 == 0):
            even_numbers.append(n)
        else:
            odd_numbers.append(n)

    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)        



def main():
    print("Hello, World!")
    sep()


if __name__ == "__main__":
    main()