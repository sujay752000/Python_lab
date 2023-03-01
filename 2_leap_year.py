def leap_check(year):
    """
    400 kond divide chyan pattunna ellaa year leap year
    athepole 4 kond divide chynum aa athe yaer 100 kond divide chyan pattatha year um leap year aan
    """
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True

    return False


current_year = int(input("Enter the initial year : "))
final_year = int(input("Enter the final year : "))

for i in range(current_year, final_year + 1):
    if leap_check(i):
        print(f"{i} - Leap year")
    else:
        print(f"{i} - Not Laep year")


"""
leap year = 2000, 2004, 2024, 2028
not leap year = 1800, 1900, 2100, 2200, 2300,
"""