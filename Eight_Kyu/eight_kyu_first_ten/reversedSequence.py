# 10. Grasshopper - Grade book, Tue, 9/04/23

# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]


def reverse_seq(n):
    arr = []
    num = n

    while num > 0:
      arr.append(num)
      num = num - 1 
    return arr

   

