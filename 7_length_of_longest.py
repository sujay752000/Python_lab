lst = ["lion", "elephant", "horse", "hippopotamus"]

max_length = 0

for i in lst:
    if len(i) > max_length:
        max_length = len(i)

for i in lst:
    if len(i) == max_length:
        print(i)
        