#21. Jaden Casing Strings, Wed, 10/04/23

# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):
    lowercase_str = string.lower()
    lowercase_list = lowercase_str.split()  # converts string to list
    changed_list = []
    for x in lowercase_list:
       titledWord = x.capitalize() 
    #    Using str.capitalize() in Python capitalizes the first letter of a string and ensures the rest of the characters are in lowercase. T
       changed_list.append(titledWord)
    changed_string = " ".join(changed_list) 
    # Changing the list back into a string, joined by " "

    return changed_string

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
