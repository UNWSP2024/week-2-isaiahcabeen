def average_age():
    print("Start by entering your friends ages")

average_age()

age_1 = float(input("Enter age friend 1:"))
age_2 = float(input("Enter age friend 2:"))
age_3 = float(input("Enter age friend 3:"))
age_4 = float(input("Enter age friend 4:"))
age_5 = float(input("Enter age friend 5:"))

avg_age = (age_1 + age_2 + age_3 + age_4 + age_5) / 5

print("The average age is:", avg_age)
