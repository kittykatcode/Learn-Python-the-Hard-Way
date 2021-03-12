formatter = " {} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format( True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
        "try some thing new",
        "lil silly may be",
        "who cares",
        "you should commit sucide , no one cares about you"

))
