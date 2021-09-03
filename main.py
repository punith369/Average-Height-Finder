student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

avg_height = 0
for height in student_heights:
    avg_height += height

total_height = ((avg_height) / len(student_heights))

print(round(total_height))



