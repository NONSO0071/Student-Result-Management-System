# Student Result Management System

student_name = input("Enter student name: ")

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))

total = score1 + score2 + score3
average = total / 3

print("\n--- Student Result ---")
print("Name:", student_name)
print("Total Score:", total)
print("Average Score:", average)
