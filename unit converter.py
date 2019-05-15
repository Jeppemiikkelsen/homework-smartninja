while True:
    print("Hi there! You can use this program for converting kilometers to miles")
    kilometers = float(input("type in how many kilometers you want to convert into miles: "))
    miles = str(kilometers * float(0.6214))
    string2 = " kilometers = "
    string4 = " miles"
    print("{0}{1}{2}{3}".format(kilometers, string2, miles, string4))
    again = input("Would you like to do another conversion? yes or no: ")
    if again == "no":
        print ("Thank you for using the program, please tell your friends about this - Goodbye")
        break

