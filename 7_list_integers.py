lst1 = [2, 5, 10, 2, 8, 4]
lst2 = [5, 4, 2,  7, 9, 20, 3]

if len(lst1) == len(lst2):
    print(f"Both have same length i,e {len(lst1)}")
else:
    print(f"Length of first list = {len(lst1)}\nLength of second list = {len(lst2)}\n")

if sum(lst1) == sum(lst2):
    print(f"Both have same length i,e {sum(lst1)}")
else:
    print(f"sum of first list = {sum(lst1)}\nsum of second list = {sum(lst2)}\n")

for i in set(lst1):
    if i in set(lst2):
        print(f"{i} is in both list")
