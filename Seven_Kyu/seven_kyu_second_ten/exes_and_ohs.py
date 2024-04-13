#35. Exes and Ohs, Thu, 11/04/23

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):

    lowercase = s.lower()
    str_to_list = list(lowercase)

    x_count = 0
    o_count = 0

    for x in str_to_list:
        if x == "x":
            x_count = x_count + 1

    for o in str_to_list:
        if o == "o":
            o_count = o_count + 1    
         
    return x_count == o_count

print(xo("oooxx"))