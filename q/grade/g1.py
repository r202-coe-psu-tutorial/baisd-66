grades = [g.strip() for g in input("Input: ").split(",")]

grade_points = 0

for g in grades:
    if g == "A":
        grade_points += 4
    elif g == "B+":
        grade_points += 3.5
    elif g == "B":
        grade_points += 3
    elif g == "C+":
        grade_points += 2.5
    elif g == "C":
        grade_points += 2
    elif g == "D+":
        grade_points += 1.5
    elif g == "D":
        grade_points += 1
    elif g == "E":
        grade_points += 0.5

average_point = grade_points / len(grades)

grade = "I"
if average_point >= 3.75:
    grade = "A"
elif average_point >= 3.25:
    grade = "B+"
elif average_point >= 2.75:
    grade = "B"
elif average_point >= 2.25:
    grade = "C+"
elif average_point >= 1.75:
    grade = "C"
elif average_point >= 1.25:
    grade = "D+"
elif average_point >= 0.75:
    grade = "D"
else:
    grade = "E"

print("Output:", grade)
