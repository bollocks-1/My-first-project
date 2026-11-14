score = int(input("Enter the Student's score (0-100)"))
if score>=90:
 grade="A"
elif score>=75:
 grade="B"
elif score>=50:
 grade="C"
else: grade = "F"

if score>=50:
 status="Pass"
else:
  status="Fail"

  print(f"Your grade is {grade}")
