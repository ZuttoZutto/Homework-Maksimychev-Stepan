"""Task 1. Kontrolnayia"""

s = input().strip()
parts = s.split('student_')
students = []
for part in parts:
    if not part:
        continue
    num = part[:3]
    score = int(part[3:])
    students.append((num, score))
if students:
    max_score = max(score for _, score in students)
    best = [num for num, score in students if score == max_score]
    print('-'.join(best))