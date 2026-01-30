
def toDict():
    l1 = [1, 2, 2, 3, 3, 3]
    freq_dict = {}

    for i in l1:

        if(i in freq_dict):
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1


    print("Frequency Dictionary:", freq_dict)



def main():
    toDict()

if __name__ == "__main__":
    main()     