# Dictionaries (think of as hashtables in java)

my_dictionary = {"Name":"Test Subject 207", "Address":"207 Ford Street"}

# we can get values from the key

# prints "Test Subject 207"
print(my_dictionary["Name"])
# prints 207 Ford Street
print(my_dictionary["Address"])



# A dictionary inside a dictionary with a list
my_complicated_dictionary = {"Food": {"Name":"Eggs", "Nutritional Values":[0, 8, 4]}, "Website":{"Google":{"Main:":"google.com", "Maps":"maps.google.com"}}}
print(my_complicated_dictionary)

# how can we get the Nutritional value list?
print(my_complicated_dictionary["Food"]["Nutritional Values"])

# how can we get the last value in that list? (work inside out)
print(my_complicated_dictionary["Food"]["Nutritional Values"][-1])

# how to get the website maps.google.com ?
print(my_complicated_dictionary["Website"]["Google"]["Maps"])

# how to change values in the dictionary?
print("Before:")
print(my_complicated_dictionary["Food"]["Name"])
print("After:")
my_complicated_dictionary["Food"]["Name"] = "Potato"
print(my_complicated_dictionary["Food"]["Name"])


# how to add keys? just name One
my_complicated_dictionary["ID"] = 101
print(my_complicated_dictionary)
