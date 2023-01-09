from math import fsum

lst = []
max_range = int(input("Enter the total number of numbers you want to add : "))
for i in range(1, max_range + 1):
    lst.append(int(input(f"Enter the {i} th value : \n")))

print(f"The sum is {fsum(lst)}")
