# Lists can be thought of as Pythons arrays

# a simple integer list
integerList = [5, 6, 7]

# printing an elment in a Lists
print(integerList[0])


# valid with multiple data types in a list including another list!
multipleList = [5, "Hello", 10, "World", True, False, [5, 5, 5], integerList]
print(multipleList)


# Unlike Strings, Lists are mutable

beforeList = ['h', 'e', 'l', 'l', 'o']
print("Before changes: ")
print(beforeList)

# change an indexes
beforeList[0] = 'T'
print("After changes: ")
print(beforeList)


# poping a Lists
last_element = beforeList.pop()
print(last_element)


# reversing a List
beforeList.reverse()
print(beforeList)



# sorting a List
beforeList.sort()
print(beforeList)

# nested lists
nested_list_one = [5, 6, 7, [4, 5, 6]]
# print out the nested list since its at index 3
print(nested_list_one[3])

# print get the index 1 inside the nested list
print(nested_list_one[3][1])

# list comprehensions
nested_list_two = [[1, 2, 3], [4,5,6], [7,8,9]]

# get the first row values
first_row = [row[0] for row in nested_list_two]

# this will return [1, 4, 7]
print(first_row)
