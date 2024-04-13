#34. Descending Order, Thu, 11/04/23

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    num_to_str = str(num)
    str_to_list = list(num_to_str)
    
    num_arr = []
    for x in str_to_list:  
        num_arr.append(int(x))

    num_arr.sort(reverse=True) # reverse array in descending order

    str_arr = []
    for char in num_arr:
        str_arr.append(str(char))

        descending_str = "".join(str_arr)
        back_to_num = int(descending_str)

    return back_to_num


print(descending_order(42145))