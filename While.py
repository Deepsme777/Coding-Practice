while True :
    name = input("Enter Your Name : ")
    if name == "" :
        print("Bro print Somethting")
    else :
        print("you name is : " + name)

        age = int(input("Enter your age : "))
        age = age + 1
        if age < 18 :
            print("Your are Minor")
        elif 18 <= age <= 100 :
            print("Your are Major")
        else : 
            print("your are Soo OLD")
        break
