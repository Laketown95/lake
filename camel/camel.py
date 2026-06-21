#Converts camel case to snake case using input
camel = input("camelCase: ")
 # name ouput in snakecase
print("snake_case: ", end="")


for c in camel:
    # first_name output in snake case
    if c.islower():
        print(c, end="")
    #preferred_first_name output in snake case
    if c.isupper():
        print("_", c.lower(), end="" , sep="")

print()
