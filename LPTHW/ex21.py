def add(a,b):
    print(f"Adding {a} = {b}")
    return a+b
def sub(a,b):
    print(f"subtracting {a} - {b}")
    return a-b
def multi(a,b):
    print(f"multiplying {a} * {b}")
    return a*b
def divd(a,b):
    print(f'dividing {a}/{b}')
    return a/b

print("lets do some maths")

Age = add(30,5)
height = sub(175,5)
weight = multi(90,2)
Iq = divd(100,4)

print(f" AGE : {Age}, HEIGHT : {height}, WEIGHT: {weight}, IQ: {Iq}")

print("here is a puzzel")

what = add(Age, sub(height,multi(weight,divd(Iq,2))))

print("that becomes", what , "can you do it by hand")
