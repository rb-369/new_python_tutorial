# 1. Total Revenue from Active Customers
# Problem Statement
# You are given a list of customer dictionaries.
# Each customer has:
# • name
# • purchases → list of purchase amounts
# • active → boolean
# Calculate the total revenue generated only by active customers, but:
# • Ignore purchase amounts less than 100
# • Apply a 10% tax to each valid purchase before summing

customers = [
    {"name": "A", "purchases": [50, 200, 300], "active": True},
    {"name": "B", "purchases": [500, 20], "active": False},
    {"name": "C", "purchases": [150, 250], "active": True}
]

# Output
# 990.0

def eg(d):
    if d.get("active") == True:
        return d
    else:
        pass

def cust():
    
    act_cust = list(filter(eg, customers))
    print(act_cust)

    sum_amt = []

    amtA =0
    for c in act_cust:
        # valid = list(filter(lambda a: a>100, c.get("purchases") ))

        for p in c.get("purchases"):
            if p < 100:
                continue
            else:
                sum_amt.append(p + p/10)

    print(sum(sum_amt))            



# 2. Problem Statement
# You are given a list of products as tuples:

#  Task:
# • Keep only products in category "Electronics"
# • Apply a 20% discount
# • Return the total discounted price
# Input
products = [
    ("Laptop", "Electronics", 1000),
    ("Shirt", "Clothing", 50),
    ("Phone", "Electronics", 500)
]
# Output:
# 1200.0

def pro():

    elec_pro = list(filter(lambda x: x[1] == "Electronics", products))
    dis_price = list(map(lambda x: x[2]*0.8, elec_pro))
    print(sum(dis_price))


# 3. Student Weighted Score Calculator
# Problem Statement
# You are given a list of students:

# Task:
# • Keep students whose average is ≥ 60
# • Increase each mark by 5 grace marks
# • Compute the total of all updated marks
# Input
students = [
    {"name": "A", "marks": [50, 60, 70]},
    {"name": "B", "marks": [30, 40]},
    {"name": "C", "marks": [80, 90]}
]

def stud():

    s2 = list(filter(lambda x: sum(x.get("marks"))/len(x.get("marks")) >= 60, students))

    s3 = list(map(lambda x: sum(x.get("marks")) + len(x.get("marks"))*5, s2))
        
    print(sum(s3))

# Output: 
# 365
def main():
    # cust()
    # pro()
    stud()

if __name__ == "__main__":
    main()