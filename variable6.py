name=input("Enter your name: ")
print("Name: ", name.title())

english_score=float(input("English: "))
math_score=float(input("Maths: "))
coding_score=float(input("Computer Science: "))

all_scores=[english_score, math_score, coding_score]

total= round(english_score + math_score + coding_score, 2)
print("Total: ", (total))
average= round(total/3, 2)
print("Average: ", (average))
highest= round(max(all_scores),2)
print("Highest: ", (highest))
lowest= round(min(all_scores),2)
print("Lowest: ", (lowest))
