int_lst = []

limit = int(input("How many numbers you want to enter in ? : "))
for i in range(0, limit):
    int_lst.append(int(input(f"Enter the {i + 1} number : ")))
    if int_lst[i] > 100:
        int_lst[i] = "over"

print(int_lst)
