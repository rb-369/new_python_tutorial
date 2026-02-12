

# 1. Average Salary Excluding Min and Max (Using Map & Filter)

# Problem Statement
# You are given a list of dictionaries where each dictionary represents an employee with name and salary.

# Remove the employees with the minimum and maximum salary, then return the average salary of the remaining employees.

# Input

employees = [
    {"name": "A", "salary": 30000},
    {"name": "B", "salary": 50000},
    {"name": "C", "salary": 40000},
    {"name": "D", "salary": 60000}
]

def avg(a):

    return a

def get_sal(emp):
    return emp["salary"]

def map_eg():
    sals = list(map(get_sal, employees))
    print(sals)
    min1 = min(sals)
    max1= max(sals)

    filter_sal = []
    
    for i in sals:
        if i == min1 or i==max1:
            continue
        else:
            filter_sal.append(i)

    avg = sum(filter_sal)/len(filter_sal)
    print(avg)

# 4. Convert & Filter Product Prices

# Problem Statement
# You are given a list of tuples (product_name, price_in_dollars).
# Convert prices to INR (1 USD = 83 INR) and return only products costing more than ₹3000.

# Input

products = [
    ("Pen", 10),
    ("Bag", 50),
    ("Shoes", 60)
]

def to_inr(val):
    return val*83 > 3000

def eg2():
    
    pr=[]
    for p in products:
        prices = list(map(to_inr, p))
        print(prices[1])
        
        
    for p in prices:
        for i in p:
            if(i > 3000):
                pr.append(i)
            else:
                continue    

    print(pr)
    

# Output

# [("Bag", 4150), ("Shoes", 4980)]





# 2. Filter Valid Email Domains

# Problem Statement
# You are given a list of email addresses. Return a list of usernames (part before @) whose email domain belongs to a given set of allowed domains.

# Input

emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com"]
allowed_domains = {"gmail.com"}
# Output

# ["alice", "carol"]
usernames = []

def valid():

    for e in emails:
        if e.split("@")[1] not in allowed_domains:
            continue
        else:
            mark = e.find("@")
            usernames.append(e[:mark])

    print(usernames)


def main():
    print("MAP")
    # map_eg()
    # valid()
    eg2()

if __name__ == "__main__":
    main()