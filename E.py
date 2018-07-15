from collections import defaultdict

arrival = defaultdict(int)
departure = defaultdict(int)
with open('input.txt') as input_:
    log_count = int(input_.readline()[:-1])
    current_day = int(input_.readline()[:-1])
    for line in input_:
        direction, day_number, clients_count = line.split()
        day_number = int(day_number)
        clients_count = int(clients_count)
        if direction == "arrival":
            arrival[day_number] += clients_count
        elif direction == "departure":
            departure[day_number] += clients_count
        else:
            raise Exception('Unknown {}'.format(direction))

in_hotel_clients = 0
mefodiy = 0
kirill = 0
for day in range(1, current_day+1):
    even_day = day % 2 == 0
    in_hotel_clients += arrival.get(day, 0)
    in_hotel_clients -= departure.get(day, 0)
    if even_day:
        kirill = in_hotel_clients if in_hotel_clients > kirill else kirill
    else:
        mefodiy = in_hotel_clients if in_hotel_clients > mefodiy else mefodiy

print(mefodiy, kirill)
