print("lets practice everything")
print("you\'d need to know\'about escape with \\that do:")
print("\n newline and \t tab")

poem = """
\tok ok ok
whoo hoo hoo ho
ahhh\n why why why
boop poop
\n\t what a crap
"""

print("-------------")
print(poem)
print("-----------")

five = 10-2+3-6
print(f"this should be five : {five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point =10000
beans, jars, crates = secret_formula(start_point)
print("with a starting point of: {}" .format(start_point))

print(f" we'd have {beans} beans, {jars} Jars and {crates} crates.")

start_point = start_point/10

print("we can also do that this way")
formula = secret_formula(start_point)

print("we'd have {} beans, {} jars and {} crates" .format(*formula))
