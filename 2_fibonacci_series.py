# using recursion
def fibonacci(limit):
    if limit == 0:
        return 0
    elif limit == 1:
        return 1
    else:
        return fibonacci(limit - 1) + fibonacci((limit - 2))


num1 = int(input("Enter a number limit to find its fibonacci series : "))
# in normal iterative way
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(3, num1 + 1):
#     c = a + b
#     a = b
#     b = c
#     print(c)

for i in range(num1):
    print(fibonacci(i))
