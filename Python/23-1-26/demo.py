

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

def main():
    print("Hello, World!")
    # sep()
    sep2()


if __name__ == "__main__":
    main()