with open("Airports.txt", "r") as f:
    data = f.readlines()

for ind,val in enumerate(data):

    data[ind] = val.split(",")

    data[ind][-1] = data[ind][-1].replace("\n", "")

aircraft_types = [["medium narrow body", "£8", "2650", "180", "8"], ["large narrow body", "£7", "5600", "220", "10"], ["medium wide body", "£5", "4050", "406", "14"]]

active = True

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
            return code, i[1]

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
                    return "Error, first class seats greater than half of standard-class seats"

            info[-1] = str(first_class)
            standard_class_seats = int(val[3]) - first_class * 2

            return " ".join(info), standard_class_seats
        
    return "Error, aircraft type not found"

def price_plan():
    with open("saved_data.txt", "r") as file:
        saved = file.readlines()

    print(saved)

    print(len(saved))

    if len(saved) < 3:
        return "Error, not enough data to calculate profit"
    
    aircraft_info = saved[2].split(" ")

    dist = 0

    if "BOH" in saved[0]:
        for airport in data:
            print(airport)
            if airport[1] == saved[1].strip():
                dist = int(airport[3])
                break
    else:
        for airport in data:
            if airport[1] == saved[1].strip():
                dist = int(airport[2])
                break

    print(dist)

    if int(aircraft_info[1]) >= dist:
        return "Error, aircraft range too short"
    
    first_class_seat_price = int(input("Enter price of first class seat"))
    standard_class_seat_price = int(input("Enter price of standard class seat"))

    standard_class_seats = int(saved[3])
    first_class_seats = int(aircraft_info[3])

    flight_cost_per_seat = int(aircraft_info[0].replace("£", "")) * dist / 100
    flight_cost = flight_cost_per_seat * (first_class_seats + standard_class_seats)
    flight_income = (first_class_seats * first_class_seat_price) + (standard_class_seats * standard_class_seat_price)
    flight_profit = flight_income - flight_cost

    print("Flight cost per seat: £" + str(flight_cost_per_seat))
    print("Flight cost: £" + str(flight_cost))
    print("Flight income: £" + str(flight_income))
    print("Flight profit: £" + str(flight_profit))

    return [flight_cost_per_seat, flight_cost, flight_income, flight_profit]


while active:
    print("1. Enter airport details\n2. Enter flight details\n3. Enter price plan and calculate profit\n4. Clear Data\n5. Quit")

    choice = input("")

    if int(choice) == 1:
        name = airport_details()

        print(name)

        if "Error" not in name:
            save(name[0], 0)
            save(name[1], 1)

    elif int(choice) == 2:
        flight = flight_details()

        if "Error" not in flight:
            save(flight[0], 2)
            save(flight[1], 3)
        else:
            print(flight)
        
    elif int(choice) == 3:
        prices = price_plan()

        if "Error" not in prices:
            save(prices[2], 4)
            save(prices[3], 5)
        else:
            print(prices)
    elif int(choice) == 4:
        clear_data()
        print("Data cleared")
    elif int(choice) == 5:
        print("Goodbye!")
        active = False
    else:
        print("Error, invalid input")

    print("\n")
