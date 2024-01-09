with open("Airports.txt", "r") as f:

    data = f.readlines()

 

for ind,val in enumerate(data):

    data[ind] = val.split(",")

    data[ind][-1] = data[ind][-1].replace("\n", "")

 

aircraft_types = [["medium narrow body", "£8", "2650", "180", "8"], ["large narrow body", "£7", "5600", "220", "10"], ["medium wide body", "£5", "4050", "406", "14"]]

print(data)


def option():

    choice = input("Please pick an option.\n1. Enter airport details\n2. Enter flight details\n3. Enter price plan and calculate profit\n4. Clear data\n5. Quit\n")

    if choice == "5":

        print("Thank you for using this program, have a wonderful day!")

        quit()

    else:

        print("That is an invalid option please try again")

option()
