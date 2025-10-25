# Simple Grade Calculator CLI

s1 = float(input("Enter your score for Subject 1: "))
s2 = float(input("Enter your score for Subject 2: "))
s3 = float(input("Enter your score for Subject 3: "))

total = s1 + s2 + s3
average = total / 3

if average >= 80:
    grade = 'A'
elif average >= 70:
    grade = 'B'
elif average >= 60:
    grade = 'C'
elif average >= 50:
    grade = 'D'
else:
    grade = 'F'

print("\n---Results--- ")
print("Total Score: ", total)
print("Average Score: ", average)
print("Grade: ", grade)