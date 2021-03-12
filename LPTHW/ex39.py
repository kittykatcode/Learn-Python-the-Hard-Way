#creat mapping of the states to the abbrivation
states = {
'Oregon': 'OR',
'FLorida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}

# creat a basic set of sates and some cities

cities = {
'CA': 'San francisco',
'MI': 'Detroit',
'FL': 'Jacksonvile'
}

#add more cities
cities['NY']= 'New York'
cities['OR']= 'portland'

#print out some cities
print('-'*20)
print("NY state has : ",cities['NY'])
print("OR state has : ",cities['OR'])

#print some states
print("-"* 20)
print("Michigan's abbreviation is :", states["Michigan"])
print("FLorida's abbrivation is: ", states["FLorida"])

#do it by using the state then cites dict
print("-"*10)
print("Michigan has: ", cities[states['Michigan']])
print("FLorida has: ", cities[states['FLorida']])

#print every state abbreviation
print('-'*20)
for a,b in list(states.items()):
    print(f"{a} is abbrivated {b}")

#print city in states
print("-"*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now both at same time
print("-"*20)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-"*10)
#safely ger abbreviation by state that might not be there

state = states.get("Texas")
if not states:
    print("sorry, no Texas")

# get city with a default value
city = cities.get("TX", 'does not exist')
print(f"the city for the state 'TX' is: {city}")
