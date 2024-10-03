year = int(input("Введите год: "))

is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap_year:
    print(f"{year} год является високосным.")
else:
    print(f"{year} год не является високосным.")