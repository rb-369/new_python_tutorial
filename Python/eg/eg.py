#reverse list

list1 = [1, 2, 3, 4, 5]
list1.reverse()
print("Reversed List:", list1)

dict1 = {'a': 1, 'b': 2, 'c': 3}

l2 = [1, [1,2,3, [12, 13, 14, [1,2,3]], list(dict1)], 3, 4, 5]
l2.reverse()
print("Reversed List:", l2)