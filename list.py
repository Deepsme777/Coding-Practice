cars = ["Mclaren" , "Ferrari" , "BMW" , "Audi" , "Mercedes"]

for x in cars :
    print(x)

#  modify list items
cars[1] = "Lambogirhini"

print(cars)
for x in cars :
    print(x)

# add list items
cars.extend(["Porsche" , "Pagani"])
print(cars)


# remove items in list
cars.pop(3)
print(cars)

# for length in lists
length = len(cars)
print(length)

print(cars[1])
print(cars[1:3])

print("----------------------")

# for insert in ists
cars.insert(1, "BMW")
for x in cars :
    print(x)

cars.clear()
for x in cars :
    print(x)


print("Thse list is cleared now.")
print(cars)