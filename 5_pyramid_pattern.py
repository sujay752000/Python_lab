limit = int(input("Enter limit : "))

for i in range(1, limit):
    for j in range(1, i + 1):
        print(j * i, " ", end="")
    print()
