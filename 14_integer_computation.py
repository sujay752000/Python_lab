num = int(input("Enter a number to compute n+nn+nnn : "))
val = 0

for i in range(1, num + 1):
    val = val + num ** i

print(val)