from sys import argv
script, user_name = argv
prompt = '>'

print(f"Hey {user_name}, I'm the {script} script")
print(" I would like to ask you few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"where do you live {user_name} ?")
lives = input(prompt)

print(f"what kind of computer do you have?")
computer = input(prompt)

print(f"""

Alright, so you saud {likes} about linking me. You live in {lives},
not sure where that is. And you hvae a {computer} computer. Nice ..

""")
