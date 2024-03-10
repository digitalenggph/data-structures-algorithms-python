# TODO 1.  Expense Exercise

expense_list = [("January", 2200), ("February", 2350), ("March",2600),
                ("April", 2130), ("May", 2190)]

# Question 1.1
question_1_1 = expense_list[1][1]-expense_list[0][1]
print(f"Extra expense Feb vs Jan = {question_1_1}")

# Question 1.2
total_expense_quarter_one = 0
for month in range(0,3):
    total_expense_quarter_one += expense_list[month][1]

question_1_2 = total_expense_quarter_one
print(f"Total expense for the first quarter = {question_1_2}")

# Question 1.3
equals_2000 = False
for month in range(0, len(expense_list)):
    if expense_list[month][1] == 2000:
        equals_2000 = True

if equals_2000:
    print(f"There is a monthly expense that is exactly 2000 dollars")
else:
    print(f"There is no monthly expense that is exactly 2000 dollars")

# Question 1.4
expense_list.append(("June", 1980))
print(expense_list)

# Question 1.5
expense_list[3] = ("April", expense_list[3][1] - 200)
print(expense_list[3])

# TODO 2. Super Hero exercise

list_heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# Question 2.1
print("\n")
print(len(list_heroes))

# Question 2.2
list_heroes.append("black panther")
print(list_heroes)

# Question 2.3
list_heroes.remove("black panther")
list_heroes.insert(2, "black panther")
print(list_heroes)

# Question 2.4
list_heroes[1], list_heroes[3] = "doctor strange", "doctor strange"
print(list_heroes)

# Question 2.5
list_heroes = sorted(list_heroes)
print(list_heroes)

# TODO 3. Odd number exercise

user_odd_input = int(input("Input maximum number for the list of odd numbers. "))

list_of_odd_numbers = []

for i in range (1, user_odd_input+1):
    if i % 2 != 0:
        list_of_odd_numbers.append(i)

print(list_of_odd_numbers)




