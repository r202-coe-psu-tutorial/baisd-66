def get_average_grade_points(grades):
    grade_points = 0
    GRADE_POINTS = {
        "A": 4,
        "B+": 3.5,
        "B": 3,
        "C+": 2.5,
        "C": 2,
        "D+": 1.5,
        "D": 1,
        "E": 0.5,
    }

    average_point = sum([GRADE_POINTS.get(g, 0) for g in grades]) / len(grades)
    return average_point


def grading(point):
    grade = "I"
    if point >= 3.75:
        grade = "A"
    elif point >= 3.25:
        grade = "B+"
    elif point >= 2.75:
        grade = "B"
    elif point >= 2.25:
        grade = "C+"
    elif point >= 1.75:
        grade = "C"
    elif point >= 1.25:
        grade = "D+"
    elif point >= 0.75:
        grade = "D"
    else:
        grade = "E"

    return grade


if __name__ == "__main__":
    # input
    grades = [g.strip() for g in input("Input: ").split(",")]

    # process
    points = get_average_grade_points(grades)
    grade = grading(points)

    # output
    print("Output:", grade)
