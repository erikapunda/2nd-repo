name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")

# First approach
print("Hello ", name, "you are ", age, "years old and live in ", location)

# Second approach %
print ("second approach")
print("Hello %s you are %d years old and you live in %s"%(name, age, location))

# Third approach format
print("third approach")
print("Hello {} you are {} years old and you live in {}".format(name, age, location))

