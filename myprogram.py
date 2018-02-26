# python operates line-by-line. If there's an error, it works until the error.
# Numbers can just be written. String text goes in quotes.
print("Hello")
print(7+3)
a = 2
b = 3.5

print(a+b)
print(type(a+b))

# Need to tell python that an input should be a number (int or float) for it to then use the input number to do math.
q_age = input("Enter your age: ")
new_age = int(q_age) + 50

print(new_age)

# Order of operations in an equation follows "Please Excuse My Dear Aunt Sally".
# Express exponents by two multipliers: 3*2 = 6. 3**2 = 9.
print(5*(2+4)**2)

# String methods. You can use a variable in a command. The following changes the e's in "here" to i's.
c = "Here"
d = c.replace("e", "i", 1)
# The 1 means it only replaces the first instance.
# Could also just put the string instead of using a variable, like "Here".replace("e", "i", 1)
print(d)

# Print out available string methods by running `dir("")`. Can ask for `help("".method)`.

# String Indexing and Splitting
# Strings are assigned numbers in python. "Hi There!" the H is 0, i is 2, space is 3, t is 4...! is 8.
# You can use these numbers to extract parts of a string.
e = "Hi There!"
f = e[3]
print(f)

# Can also count from other direction. ! is -1, e is -2... H is -9.
print(e[-1])

# Can extract a series. A split is upper-bound exclusive. So marking 0-1 would only print 0; 0-4 only includes 0, 1, 2, 3.
# Splitting from other direction, using negative numbers still works left to right.
print(e[0:4], e[-3:-1])

# Lists
# Lists are similar to strings. But a string is made of other strings. Lists can contain other data types, like int, float, string.
# Can store files, widgets, etc. in a list. Can also index and split lists.
# Indexing system is same as for strings
# Check available methods by doing dir(list). Can also do help.
g = ["Hi", "are u down", 2, "go to this address?", 9.75]
print(g[1:4])
h = g.append("no")
print(g)

# Tuples
# Tuples are like lists, but NOT mutable (you can't change them). Thus, used for specific scenarios.
# Use parens instead of brackets. Has different dir(tuple) methods available, like "count".
i = ("Hi", "are u down", 2, "got to this address?", 9.75)
print(i)

# Dictionaries
# Like lists, but you can create the indices yourself (doesn't assign 0, 1, 2, 3 etc.).
# Use curly brackets, not brackets.
# First entry is the key and the second is the value. Strings are in quotes, numbers not.
# You can extract info from the dictionary by passing the key.
# Values can include lists, tuples, dictionaries.
j = {"Name":"John", "Surname":"Smith", "Cities":("LA", "DC", "NYC")}
print(j["Cities"][2])
