
def main():
    records = [
    (1, "alice", ["login", "view", "logout"]),
    (2, "bob", ["login", "view"]),
    (3, "alice", ["login", "purchase"]),
    (4, "david", ["login", "view", "purchase", "logout"]),
    ]

    uni_set = set()
    for record in records:
        uni_set.add(record[1])

    print("Unique Usernames: ",uni_set)  

    act_list = []
    for i in range(0, 4):
        
        for act in records[i][2]:
            act_list.append(act)

    print(act_list)

    # counts = {act_list[0]:0,act_list[1]:1,act_list[2]:0,act_list[3]:0}
    counts_act = set(act_list)
    # counts = {act_list[0]: 0, act_list[1]: 0,act_list[2]: 0,act_list[3]: 0}
    counts  = {}

    # for i in range(0, 4):
    #     counts[act_list[i]] =+ 1
    #     if act in counts_act:
    #         counts[act_list[i]] =+ 1

    for act in act_list:
        if act in act_list:
            counts[act] +=1
        else:
            counts[act] =1    


    # act_dict = dict(zip(act_list, counts))
    print(counts)       

    

if __name__ == "__main__":
    main()