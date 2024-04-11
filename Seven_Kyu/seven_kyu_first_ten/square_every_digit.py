#28. Square Every Digit, Wed, 10/04/23

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!

def square_digits(num):
    
    num_str = str(num)
    str_list = list(num_str)

    num_list_squared = []
    for char in str_list:
     squared_num = int(char) * int(char)
     squared_str = str(squared_num)
     num_list_squared.append(squared_str)
    
    squared_num_str = "".join(num_list_squared)

    actual_squared_num = int(squared_num_str)

    return actual_squared_num

print(square_digits(765))