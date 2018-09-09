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
