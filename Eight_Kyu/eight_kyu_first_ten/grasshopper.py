# 9. Grasshopper - Grade book, Tue, 9/04/23

# Grade book

# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    sum = (s1 + s2 + s3) / 3

    if sum >= 90 and sum <= 100:
      return "A"
    elif sum >= 80 and sum < 90:
       return "B"
    elif sum >= 70 and sum < 80:
       return "C"
    elif sum >= 60 and sum < 70:
       return "D"
    elif sum < 60 and sum >= 0:
       return "F"
     
