seasons = ("winter", "spring", "summer", "autumn")
month = int(input("Enter a month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])
elif 3 <= month <= 5:
    print(seasons[1])
elif 6 <= month <= 8:
    print(seasons[2])
elif 9 <= month <= 11:
    print(seasons[3])