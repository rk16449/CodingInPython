# Using Strings in python


# two types, double quote or single quote
a_string = 'this is a string'
b_string = "this is also a string"
ab_string = "this String's has an apostraphe"
print(ab_string)





# how to index strings, use square brackets

# this will print: t
print(a_string[0])

# this will print: h
print(a_string[1])

# negative indexes also work (it will start at the back of the string)
print(a_string[-1])


# how to Slice strings, use colon

# this will grab everything after the 4th index
# it will print: 'is a string'
print(a_string[4:])


# the reverse can also happens
# this is upto but not including that index
# is will print: 'this'
print(a_string[:4])

# we can also do between values
# this is grab index 1 and end but not including 3
print(a_string[1:3])

# strings in python are immutable

immutableString = 'I am immutable'

# this would give a TypeError
# immutableString[0] = 'H'

# we can always redefine the string to something different
immutableString = "H"
print(immutableString)



# Basic String methods


# this will make all letters upper case
lower_case_string = 'hello world'
upper_case_string = lower_case_string.upper()
print(upper_case_string)

# this will capitalize the first letter
no_capitals_string = 'test me'
capital_string = no_capitals_string.capitalize()
print(capital_string)

# splitting Strings
test_string = "Windows 10 is great"
split_string = test_string.split()
# this will give a string list, with each word separated by a space as a unique element
# this will give ['Windows', '10', 'is', 'great']
print(split_string)


# further splitting Strings
test_string = "Hello World"
new_string = test_string.split('e')
# this will give ['H', 'llo World']
# the e is removed
print(new_string)



# how to print format
abc = "Insert Item: {}".format("Newspaper")
print(abc)


# formating again, but with variables added

subjects = "Subject One: {english} Subject Two: {maths} ".format(maths = "Mathematics", english = "English")
print(subjects)
