# using recursion
def fact(num):

    if num <= 1:
        return 1
    else:
        return num * fact(num - 1)


num1 = int(input("Enter a numbe rto find its factorial : "))
print(fact(num1))

# in normal iterative way
# fact = 1
#
# for i in range(1, num1 + 1):
#     fact = fact * i
#
# print(fact)
