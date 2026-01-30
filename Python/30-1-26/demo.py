
def toDict():
    l1 = [1, 2, 2, 3, 3, 3]
    freq_dict = {}

    for i in l1:

        if(i in freq_dict):
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1


    print("Frequency Dictionary:", freq_dict)

# 2. Dictionary Key Check
# Problem:
# Given a dictionary and a key, return "Found" if the key exists, otherwise return "Not Found".
# Input:
# {"a": 1, "b": 2}, key = "b"
# Output:
# "Found"

def KeyCheck():
    d1 = {"a": 1, "b": 2}
    k = "b"

    if(d1.get(k)):
        print("Key Found! ")
    else:
        print("Key not found!") 

# 3. Tuple to Dictionary
# Problem:
# Given a tuple of (key, value) pairs, convert it into a dictionary.
# Input:
# (("a", 1), ("b", 2))
# Output:
# {"a": 1, "b": 2}

def tupToDict():
    t1 = (("a", 1), ("b", 2))
    d1 = dict(t1);

    print(d1)

# 4. Reverse Words
# Problem:
# Given a string, return a list of words in reverse order.
# Input:
# "data science is fun"
# Output:
# ["fun", "is", "science", "data"]    

def rev():
    s1= "data science is fun"

    l1 = list(s1.split(" "))
    print(l1)

# 5. Sum of Tuples
# Problem:
# Given a list of tuples containing two integers each, return a list of their sums.
# Input:
# [(1, 2), (3, 4), (5, 6)]
# Output:
# [3, 7, 11]

def sumOfTup():
    t1=[(1, 2), (3, 4), (5, 6)]
    l1=[t1[0][0] + t1[0][1], t1[1][0]+t1[1][1], t1[2][0] + t1[2][1]]
    res = []
    for t in t1:
        res.append(sum(t))

    print(res)
    print(l1)

# 6. String Length Map
# Problem:
# Given a list of strings, return a dictionary with each string and its length.
# Input:
# ["python", "ml", "ai"]
# Output:
# {"python": 6, "ml": 2, "ai": 2}

def strLenMap():
    l1 = ["python", "ml", "ai"]
    d1 = {l1[0]: len(l1[0]), l1[1]: len(l1[1]), l1[2]: len(l1[2])}

    print(d1)

# 7. Unique Characters
# Problem:
# Given a string, return a tuple of unique characters in the order they appear.
# Input:
# "programming"
# Output:
# ("p", "r", "o", "g", "a", "m", "i", "n")

def uniChar():
    s1 = "programming"
    uni_s1 = ""
    
    for char in s1:
        if(char in uni_s1):
            pass
        else:
            uni_s1+=char
    
    t2 = tuple(uni_s1)

    print(t2)

# 8. Filter Even Numbers
# Problem:
# Given a list of numbers, return a new list containing only even numbers.
# Input:
# [1, 2, 3, 4, 5, 6]
# Output:
# [2, 4, 6]

def eveArr():
    l1 = [1, 2, 3, 4, 5, 6]
    even_l =[]

    for i in l1:
        if(i %2 ==0):
            even_l.append(i)

    print(even_l)        

# 9. Student Average Score
# Problem:
# You are given a list of tuples where each tuple contains a student name and a list of marks. Return a dictionary mapping each student’s name (lowercase) to their average score.
# Input:
# [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
# Output:
# {"alice": 85.0, "bob": 81.67}

def avgScore():
    l1 = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]

    d1 = {l1[0][0]: ((l1[0][1][0]+l1[0][1][1])/2), l1[1][0]: ((l1[1][1][0]+l1[1][1][1]+l1[1][1][2])/3)}

    

    print(d1)

def main():
    toDict()
    KeyCheck()
    tupToDict()
    rev()
    sumOfTup()
    strLenMap()
    uniChar()
    eveArr()
    avgScore()

if __name__ == "__main__":
    main()     