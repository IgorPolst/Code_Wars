# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

def str_count(strng, letter):
    return len(strng)-len(strng.replace(letter, ""))


print (str_count('hello', 'l'), 2)
print (str_count('hello', 'e'), 1)
print (str_count('codewars', 'c'), 1)
print (str_count('ggggg', 'g'), 5)
print (str_count('', 'z'), 0)
print (str_count('hello world', 'o'), 2)