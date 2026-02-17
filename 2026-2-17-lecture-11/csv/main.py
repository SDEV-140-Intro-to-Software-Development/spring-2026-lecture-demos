# The goal is to calculate the average grade in the class

import os
import csv

with open(os.path.join("2026-2-17-lecture-11", "csv", "grades.csv.csv")) as f:
    reader = csv.reader(f)

    is_first_row = True

    class_total_averages = 0
    class_total_students = 0
    for row in reader:
        if is_first_row:
            is_first_row = False
            continue

        student_total_assignments = 0
        student_total_points = 0

        for grade in row[1:]:
            student_total_assignments += 1
            student_total_points += int(grade)

        student_avg = student_total_points / student_total_assignments
        class_total_averages += student_avg
        class_total_students += 1

    class_average = class_total_averages / class_total_students
    print(f"Class Average is: {class_average:.2f}%")
