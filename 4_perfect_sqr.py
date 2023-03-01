from math import sqrt


def even_check(num):
    str_num = str(num)
    new_str = ""
    for i in str_num:
        if int(i) % 2 == 0:
            new_str = new_str + i

    if new_str == str_num:
        return True
    else:
        return False


def perfect_square(num):
    if int(sqrt(num)) * int(sqrt(num)) == num:
        return True
    else:
        return False


result_lst = []
initial = int(input("Enter initial range : "))
final = int(input("Enter final range : "))

for i in range(initial, final + 1):
    if even_check(i) == True and perfect_square(i) == True:
        result_lst.append(i)

print(result_lst)