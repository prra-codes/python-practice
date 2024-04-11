#26. Is it a letter?, Wed, 10/04/23

# Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.

def is_it_letter(s):
    letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w","v",  "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W","V" "X", "Y", "Z"]
    
    for letter in letter_list:
        if s == letter:
            return True
        
    return False
    