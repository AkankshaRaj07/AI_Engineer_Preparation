# Exercise 1 — Data types
# Easy

# Create variables representing a student's name, age, CGPA, enrollment status and skills.

# Print their values and data types.


name = "Akanksha Kumari"
age = 23
cgpa = 9.21
enrollment_status = True
skills = ["Python", "Java", "Full Stack Development"]
print("Name: ", name, "Type:", type(name))
print("Age: ", age, "Type:", type(age))
print("CGPA: ", cgpa, "Type:", type(cgpa))
print("Enrollment Status: ", enrollment_status, "Type:", type(enrollment_status))
print("Skills: ", skills, "Type:", type(skills))


# Exercise 2 — String manipulation
# Intermediate

# Given:
# s = "artificial intelligence engineering"



# - Count the total characters.
# - Count the number of words.
# - Convert the string to uppercase.
# - Extract the word "intelligence" using slicing.
s = "artificial intelligence engineering"
print("length: ", len(s))
print("words: ", len(s.split()))
print("uppercase: ", s.upper())
print("sliced: ", s[11:23])