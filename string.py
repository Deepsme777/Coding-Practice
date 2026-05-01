Name = "G Deepakkumar"
print(Name)
print(type(Name))
age = 19
print(age)
print(type(age))

# add str + int
age = str(age)
print(Name + " " + age)
print("Your Name is : " + Name)
print("Your age is : " + age)
print("No of alpha in your name : " + str(len(Name)))

name_1 = "lakshaya"

print(Name.find("a"))
print(name_1.capitalize())
print(name_1.upper())
print(name_1.count("a"))
print(name_1.isdigit())
print(name_1.isalpha())
print(name_1.replace("a" , "A"))

print("----------------------")

# String Slicing

name_2 = "Deepakkumar"

first_name = name_2[0:6]
print(first_name)

last_name = name_2[-5:]
print(last_name)

reverse_name = name_2[::-1]
print(reverse_name)

print("----------------------")

# slice function

web_1 = "www.Co-Sync.com"
web_2 = "https://www.CO-SYNC.com"

slice_1 = slice(4, 11)
print(web_1[slice_1])

slice_2 = slice(12, 19)
print(web_2[slice_2])


# to cappitalize the lower case  and to lower the upper case Aquired from user input

def swap_case(s):
    string = ""

    for i in s:
        if i == i.upper():
            string = string + i.lower()
        
        elif i == i.lower():
            string = string + i.upper()

        else:
            string = string + i

        return string


print("------------------------")