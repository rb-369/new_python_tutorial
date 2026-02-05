def main():
    # --------------------
    # SET EXAMPLES
    # --------------------

    # Sets automatically remove duplicate values
    numbers_set = {1, 2, 3, 4, 3}
    print("Initial set:", numbers_set)

    # Add an element to the set
    numbers_set.add(6)
    print("After adding 6:", numbers_set)

    # Remove and return a random element
    removed_element = numbers_set.pop()
    print("Popped element:", removed_element)
    print("Set after pop:", numbers_set)

    # Convert a list to a set (removes duplicates)
    numbers_list = [1, 2, 2, 2, 3, 5, 7]
    unique_numbers = set(numbers_list)
    print("Unique numbers from list:", unique_numbers)

    # Iterate over a set
    print("Iterating over set:")
    for num in unique_numbers:
        print(num)

    # --------------------
    # DICTIONARY EXAMPLES
    # --------------------

    # Create a dictionary
    person = {"name": "rb", "age": 17}
    print("\nInitial dictionary:", person)

    # Access a value by key
    print('Name:', person["name"])

    # Update a value
    person["age"] = 18
    print("After updating age:", person)

    # Iterate over dictionary
    print("Iterating over dictionary:")
    for key, value in person.items():
        print(f"{key}: {value}")

    # Delete a key
    del person["age"]
    print("After deleting age:", person)

    # Clear the dictionary
    person.clear()
    print("After clearing dictionary:", person)


if __name__ == "__main__":
    main()
