

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

def sep2():
    word = input("Enter a without space word: ")
    if(' ' in word):
        print("Invalid input! Please enter a word without spaces.")
        return
    vowels = 'aeiouAEIOU'
    vowel_chars = []
    consonant_chars = []
    for char in word:
        if char in vowels:
            vowel_chars.append(char)
        else:
            consonant_chars.append(char)

    print(f"Total {len(vowel_chars)} Vowels in the word:", vowel_chars)
    print(f"Total {len(consonant_chars)} Consonants in the word:", consonant_chars)  

def eg():

    lim = int(input("Enter the limit: "))
    if(lim < 0):
        print("Invalid limit! Limit must be non-negative.")
        return
    l1 = []
    for i in range(1, lim+1):
        l1.append(int(input(f"Enter element {i}: ")))

    print("Original List:", l1)    

    for i in range(len(l1)):
        if(i != 0):
            l1[i] = l1[i] + l1[i-1]

    print("Cumulative addition of List:", l1)  
    str1 = "seriuh" 
    print(str1[:-1])        

def longest_prefix():

    l1 = []
    n = int(input("Enter number of strings: "))
    for i in range(n):
        s = input(f"Enter string {i+1}: ")
        l1.append(s)

    longest_prefix = ""    

    for i in range(len(l1[0])):
        char = l1[0][i]
        for j in range(1, n):
            if i >= len(l1[j]) or l1[j][i] != char:
                return print("Longest Common Prefix:", longest_prefix) if longest_prefix else print("No Common Prefix Found")
        longest_prefix += char
        res = longest_prefix  

    

def main():
    print("Hello, World!")
    # sep()
    # sep2()
    # eg()
    longest_prefix()


if __name__ == "__main__":
    main()