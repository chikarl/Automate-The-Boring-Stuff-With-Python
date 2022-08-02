cost = 5000
tickets = 0
total = 0
num_pass = 0
while num_pass <= 70:
    tickets = int(input("ENTER NUMBER OF TICKETS: "))
    if tickets == -1:
        total = num_pass * cost
        print("Total number if Passengers = ", num_pass)
        print("Total Amount: ", total)
        break

    num_pass = tickets + num_pass
    if num_pass > 70:
        print("Sorry max number of passengers is 70")
        num_pass = num_pass - tickets
    elif num_pass == 70:
        total = num_pass * cost
        print("Total number if passengers = ", num_pass)
        print("Total Amount: ", total)
        break

    print("Actual number if passengers = ", num_pass)
