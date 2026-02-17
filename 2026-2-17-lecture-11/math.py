import os


f = open(os.path.join("2026-2-17-lecture-11", "math-data.txt"))
total = 0
number_of_lines=0
for line in f:
    number_of_lines+=1
    total += int(line.strip())
f.close()

avg = total / number_of_lines
print("total=",total)
print("avg=",avg)




