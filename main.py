with open("Airports.txt", "r") as f:
    data = f.readlines()

for ind,val in enumerate(data):

    data[ind] = val.split(",")

    data[ind][-1] = data[ind][-1].replace("\n", "")

aircraft_types = [["medium narrow body", "£8", "2650", "180", "8"], ["large narrow body", "£7", "5600", "220", "10"], ["medium wide body", "£5", "4050", "406", "14"]]

active = True

print(data)

def clear_data():
    with open("saved_data.txt", "r") as file:
        saved = file.readlines()

    saved = []

    with open("saved_data.txt", "w") as file:
        file.writelines(saved)

def save(d, ind):
    with open("saved_data.txt", "r") as file:
        saved = file.readlines()

    for i in range(0, 4):
        saved.append("")

    saved[ind] = str(d) + "\n"

    with open("saved_data.txt", "w") as file:
        file.writelines(saved)

def airport_details():
    code = input("Please enter the three-letter airport code for the UK airport")

    if code != "LPL" and code != "BOH":

        return "Error, airport not found."

    overseas_code = input("Please enter the three-letter code for the overseas airport")

    for i in data:
        if i[0] == overseas_code:
            return i[1]

    return "Error, overseas airport code invalid"

def flight_details():
    aircraft = input("Please enter the type of aircraft to be used")

    for ind,val in enumerate(aircraft_types):
        if val[0] == aircraft:

            info = val[1:]
            first_class = int(input("Enter number of first class seats on the aircraft"))

            if first_class != 0:
                if first_class < int(val[4]):
                    return "Error, too few seats compared to minimum amount"

                elif first_class > int(val[3])/2:

                    return "Error, first class seats greater than minimum of standard-class seats"

            info[-1] = str(first_class)
            standard_class_seats = int(val[3]) - first_class * 2

            return " ".join(info), standard_class_seats

while active:
    print("1. Enter airport details\n2. Enter flight details\n3. Enter price plan and calculate profit\n4. Clear Data\n5. Quit")

    choice = input("")

    if int(choice) == 1:
        name = airport_details()

        print(name)
        
        save(name, 0)
    elif int(choice) == 2:
        flight = flight_details()

        save(flight[0], 1)
        save(flight[1], 2)

    print("\n")
