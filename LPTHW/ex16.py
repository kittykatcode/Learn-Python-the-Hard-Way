from sys import argv

script, filename = argv

print(f" we are going to erase {filename}")
print(f"If you dont want that, hit CTRL-C (^C)")
print("If you want that hit RETURN")

input("?")

print("opening the file")
target = open(filename, 'w')
print("tuncateing the file")
target.truncate()

print("now I am going to ask you for 3 lines")

line1 = input('line1: ')
line2 = input('line2: ')
line3 = input('line3: ')
print("i am goint to rite these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it",)

target.close()
