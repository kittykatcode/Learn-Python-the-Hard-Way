cars = 100
space_in_a_car = 4
driver = 30
passanger = 90
cars_not_driven = cars - driver
cars_driven = driver
carpool_capacity = cars_driven*space_in_a_car
average_passanger_per_car = passanger/cars_driven
print("there are", cars, "cars available")
print("there are only", driver, "drivers available")
print("there will be ", cars_not_driven ,"empty cars today")
print("we can transport", carpool_capacity , "people today")
print(" we have", passanger, "to carpool")
print("we need to put about", average_passanger_per_car, "per car")
# why m i doing this
