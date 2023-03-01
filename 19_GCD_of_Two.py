# def gcd_cal(num1, num2):
#     gcd = 0
#
#     maximum = max(num1, num2)
#
#     for i in range(1, maximum + 1):
#         if num1 % i == 0 and num2 % i == 0:
#             gcd = i
#
#     return gcd


num1 = int(input("Enter First number : "))
num2 = int(input("Enter second number : "))

maximum = max(num1, num2)

gcd = 0

for i in range(1, maximum + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print(f"GCD = {gcd}")

# lst = [15, 10, 20, 25]
#
# result = lst[0]
#
# for i in range(1, len(lst)):
#     result = gcd_cal(result, lst[i])
#
# print(result)

