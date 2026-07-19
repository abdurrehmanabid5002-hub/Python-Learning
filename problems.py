i = 1
while i <= 2:
    marks = []

    for j in range(3):
        marks.append(int(input(f"Enter marks {j + 1}: ")))

    marks1 = marks[0]
    marks2 = marks[1]
    marks3 = marks[2]

    total_percentage = (marks1 + marks2 + marks3) / 300 * 100

    if total_percentage > 40 and marks1 > 33 and marks2 > 33 and marks3 > 33:
        print("You are pass", total_percentage)
    else:
        print("You are fail", total_percentage)
    i += 1