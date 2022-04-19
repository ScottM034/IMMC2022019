from random import randint

#On plane figure 2 and plane figue 3, I treated the aisles as one connected long aisle, in order to add the time it would take up when blocking the walkway between aisles

beyond_blocker = []
beyond_blocker_time = []
current_blocked = {}
blocking_aisle = 0
already_blocked = []
dudes_blocking = []
shift_list_dont_delete = []
passenger_list = []
rows = 56 #Rows increase to aisles * length of aisle for the one long aisle
columns = 6
seats = rows * columns
full_seating = {}
passenger_with_seat = {}
baggage = {}
seating = []
seat_number = {}
total_walk = 0
bag_total_time = 0
total_time = total_walk + bag_total_time
people_and_rows = {}
people_and_columns = {}
walking_time = 0
bag_time = 0
people_left = 0
sat_down = []
added_time = 0
total_removed = 0
correspond_bag = []
line_up = []
groupings = [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13] , [14, 15, 16, 17, 18, 19, 20]]
seat_down_check = []
bag_time_or_shift = 0
shift_list = []
shift = 0
entering_plane = []

import random
new_groupings = random.sample(groupings, len(groupings))

ranges = [[0], [1, 2, 3, 4], [5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33, 34, 35]]
ranges_probability = [40, 14, 23, 23, 19, 12, 7, 2]
all_probs = []



for i in range(len(ranges)):
    for x in range(len(ranges[i])):
        for z in range(ranges_probability[i]):
            all_probs.append(ranges[i][x])
    



while len(passenger_list) != (seats):
    for i in range(seats):
        passenger = randint(0, (seats))
        if passenger in passenger_list:
            pass
        elif passenger == seats:
            pass
        else:
            passenger_list.append(passenger)

for i in range(len(passenger_list)):
    line_up.append(passenger_list[i])

            
for i in range(rows):
    for j in range(columns):
        row_seat_check = (columns * i) + j
        people_and_rows[row_seat_check] = i
for i in range(rows):
    if i in people_and_rows:
        pass
    else:
        people_and_rows.append(i)

for i in range(rows):
    if passenger_list[i] in people_and_rows.keys():
        pass
    else:
        passenger_list.remove(passenger_list[i])
        
    

for i in range(rows):
    for j in range(columns):
        column_seat_check = (columns * i) + j
        people_and_columns[column_seat_check] = (j + 1)


for i in range(seats):
        baggage[i] = random.choice(all_probs)

people_and_rows['0'] = 200


check_digit = 0
while True:
    while check_digit < seats:
        check_bag = 0
        new_passenger = passenger_list[check_digit]
        entering_plane.insert(0, new_passenger)
        walking_time += 1
        for i in range(len(entering_plane)):
            if entering_plane.index(entering_plane[(i)]) == int(people_and_rows.get(entering_plane[(i)])):
                    sat_down.insert(0, (entering_plane[(i)]))
                    people_left += 1
                    person_row = int(people_and_rows.get(entering_plane[(i)]))
                    person_column = int(people_and_columns.get(entering_plane[i]))
                    if person_column > 3:
                        if person_column == 4:
                            pass
                        elif person_column == 5:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 4:
                                    shift_list.append(2)
                                else:
                                    pass
                        elif person_column == 6:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 5:
                                    shift_list.append(4)
                                else:
                                    pass
                        
                    if person_column < 4:
                        if person_column == 3:
                            pass
                        elif person_column == 2:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 3:
                                    shift_list.append(2)
                                else:
                                    pass
                        elif person_column == 1:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 2:
                                    shift_list.append(4)
                                else:
                                    pass
                        
                    if check_digit < (seats - 1):
                        check_digit += 1
                    else:
                        pass
                    seat_down_check.append(entering_plane[i])
                    if int(people_and_rows.get(entering_plane[(i)])) > 41:
                        if entering_plane[i] in already_blocked: #Here we add the amount of time someone causes the walkway between aisles to be blocked
                            pass
                        else:
                            for p in range(int(baggage.get(entering_plane[i]))):
                                ind_d = passenger_list.index(entering_plane[i]) + p
                                if ind_d >= seats:
                                    ind_d -= ind_d
                                    ind_d += (seats - 1)
                                else:
                                    pass
                                if int(people_and_rows.get(passenger_list[ind_d])) > int(people_and_rows.get(entering_plane[i])):
                                    beyond_blocker.append(passenger_list[ind_d])
                                else:
                                    pass
                            if len(beyond_blocker) >= (int(people_and_rows.get(entering_plane[i])) - 41): #It checks if the line up behind the blocker goes into the walkway
                                    difference = passenger_list.index(beyond_blocker[-1])- passenger_list.index(entering_plane[i])
                                    if difference < 0:
                                        difference -= difference
                                        difference += int(baggage.get(entering_plane[i]))
                                    else:
                                        pass
                                    beyond_blocker_time = int(baggage.get(entering_plane[i])) - difference
                                    dudes_blocking.append(beyond_blocker_time)
                                    already_blocked.append(entering_plane[i]) #And then adds the amount of the time that same line behind the blocker has actually been blocking the walkway
                    elif int(people_and_rows.get(entering_plane[(i)])) < 42 and int(people_and_rows.get(entering_plane[(i)])) > 27:
                        if entering_plane[i] in already_blocked:
                            pass
                        else:
                            for p in range(int(baggage.get(entering_plane[i]))):
                                ind_d = passenger_list.index(entering_plane[i]) + p
                                if ind_d >= seats:
                                    ind_d -= ind_d
                                    ind_d += (seats - 1)
                                else:
                                    pass
                                if int(people_and_rows.get(passenger_list[ind_d])) > int(people_and_rows.get(entering_plane[i])):
                                    beyond_blocker.append(passenger_list[ind_d])
                                else:
                                    pass
                            if len(beyond_blocker) >= (int(people_and_rows.get(entering_plane[i])) - 27):
                                    difference = passenger_list.index(beyond_blocker[-1])- passenger_list.index(entering_plane[i])
                                    if difference < 0:
                                        difference -= difference
                                        difference += int(baggage.get(entering_plane[i]))
                                    else:
                                        pass
                                    beyond_blocker_time = int(baggage.get(entering_plane[i])) - difference
                                    dudes_blocking.append(beyond_blocker_time)
                                    already_blocked.append(entering_plane[i])
                    elif int(people_and_rows.get(entering_plane[(i)])) < 28 and int(people_and_rows.get(entering_plane[(i)])) > 13:
                        if entering_plane[i] in already_blocked:
                            pass
                        else:
                            for p in range(int(baggage.get(entering_plane[i]))):
                                ind_d = passenger_list.index(entering_plane[i]) + p
                                if ind_d >= seats:
                                    ind_d -= ind_d
                                    ind_d += (seats - 1)
                                else:
                                    pass
                                if int(people_and_rows.get(passenger_list[ind_d])) > int(people_and_rows.get(entering_plane[i])):
                                    beyond_blocker.append(passenger_list[ind_d])
                                else:
                                    pass
                            if len(beyond_blocker) >= (int(people_and_rows.get(entering_plane[i])) - 13):
                                    difference = passenger_list.index(beyond_blocker[-1])- passenger_list.index(entering_plane[i])
                                    if difference < 0:
                                        difference -= difference
                                        difference += int(baggage.get(entering_plane[i]))
                                    else:
                                        pass
                                    beyond_blocker_time = int(baggage.get(entering_plane[i])) - difference
                                    dudes_blocking.append(beyond_blocker_time)
                                    already_blocked.append(entering_plane[i])
                    elif int((people_and_rows.get(entering_plane[(i)]))) < 14:
                        for z in range(len(passenger_list)):
                            if int(people_and_rows.get(entering_plane[i])) <= int(people_and_rows.get(passenger_list[z])) and passenger_list.index(entering_plane[i]) > passenger_list.index(passenger_list[z]) :
                                index_difference_calc = passenger_list.index(entering_plane[i]) - passenger_list.index(passenger_list[z])
                                if (int(baggage.get(entering_plane[i]))- index_difference_calc) < 0:
                                    pass
                                else:
                                    correspond_bag.append((int(baggage.get(entering_plane[i]))) - index_difference_calc)
                            else:
                                pass
                    else:
                        pass
                    new_passenger = passenger_list[check_digit]
            elif entering_plane.index(entering_plane[(i)]) != int(people_and_rows.get(entering_plane[(i)])):
                pass
        while True:
            if len(sat_down) != 0:
                entering_plane.remove(sat_down[0])
                sat_down.remove(sat_down[0])
                added_time -= 1
                total_removed += 1
            else:
                break
        if check_digit <= (seats - 1):
            check_digit += 1
        else:
            pass

        dudes_blocking.sort(reverse=True)
        if len(dudes_blocking) > 0:
            blocking_aisle += dudes_blocking[0]
            dudes_blocking.clear()
            dudes_blocking.append(0)
        else:
            pass

        correspond_bag.sort(reverse=True)
        try:
            if correspond_bag[0] > 3:
                bag_time_or_shift += correspond_bag[0]
                check_bag = 0
                correspond_bag.clear()
                shift_list.clear()
            elif 3 in shift_list and check_bag == 1:
                bag_time_or_shift += 3
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 2 == correspond_bag[0] or 2 in shift_list and check_bag == 1:
                bag_time_or_shift += 2
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 1 == correspond_bag[0] and check_bag == 1:
                bag_time_or_shift += 1
                correspond_bag.clear()
                shift_list.clear()
                pass
            else:
                correspond_bag.clear()
                shift_list.clear()
                pass
        except IndexError:
            continue
        
    while check_digit == seats:
        for k in range(rows):
            check_bag = 0
            entering_plane.insert(k, '0')
            walking_time += 1
            for i in range(len(entering_plane)):
                if i == int(people_and_rows.get(entering_plane[(i)])):
                    if int(people_and_rows.get(entering_plane[(i)])) > 20:
                        if entering_plane[i] in already_blocked:
                            pass
                        else:
                            for p in range(int(baggage.get(entering_plane[i]))):
                                ind_d = passenger_list.index(entering_plane[i]) + p
                                if ind_d >= seats:
                                    ind_d -= ind_d
                                    ind_d += (seats - 1)
                                else:
                                    pass
                                if int(people_and_rows.get(passenger_list[ind_d])) > int(people_and_rows.get(entering_plane[i])):
                                    beyond_blocker.append(passenger_list[ind_d])
                                else:
                                    pass
                            if len(beyond_blocker) >= (int(people_and_rows.get(entering_plane[i])) - 20):
                                    difference = passenger_list.index(beyond_blocker[-1])- passenger_list.index(entering_plane[i])
                                    if difference < 0:
                                        difference -= difference
                                        difference += int(baggage.get(entering_plane[i]))
                                    else:
                                        pass
                                    beyond_blocker_time = int(baggage.get(entering_plane[i])) - difference
                                    dudes_blocking.append(beyond_blocker_time)
                                    already_blocked.append(entering_plane[i])
                    elif int((people_and_rows.get(entering_plane[(i)]))) < 21:
                        for z in range(len(passenger_list)):
                            if int(people_and_rows.get(entering_plane[i])) <= int(people_and_rows.get(passenger_list[z])) and passenger_list.index(entering_plane[i]) > passenger_list.index(passenger_list[z]) :
                                index_difference_calc = passenger_list.index(entering_plane[i]) - passenger_list.index(passenger_list[z])
                                if (int(baggage.get(entering_plane[i]))- index_difference_calc) < 0:
                                    pass
                                else:
                                    correspond_bag.append((int(baggage.get(entering_plane[i]))) - index_difference_calc)
                            else:
                                pass
                    else:
                        pass
                    sat_down.insert(0, (entering_plane[(i)]))
                    people_left += 1
                    person_row = int(people_and_rows.get(entering_plane[(i)]))
                    person_column = int(people_and_columns.get(entering_plane[i]))
                    if person_column > 2:
                        if person_column == 3:
                            pass
                        elif person_column == 4:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 3:
                                    shift_list.append(2)
                                else:
                                    pass
                        
                    if person_column < 3:
                        if person_column == 2:
                            pass
                        elif person_column == 1:
                            for z in range(len(seat_down_check)):
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 2:
                                    shift_list.append(2)
                                else:
                                    pass
                    check_digit += 1
                elif entering_plane.index(entering_plane[(i)]) != int(people_and_rows.get(entering_plane[(i)])):
                    pass
            while True:
                if len(sat_down) != 0:
                    entering_plane.remove(sat_down[0])
                    sat_down.remove(sat_down[0])
                    added_time -= 1
                    total_removed += 1
                else:
                    break
            check_digit += 1 
            
            dudes_blocking.sort(reverse=True)
            if len(dudes_blocking) > 0:
                blocking_aisle += dudes_blocking[0]
                dudes_blocking.clear()
                dudes_blocking.append(0)
            else:
                pass
            correspond_bag.sort(reverse=True)
        try:
            if correspond_bag[0] > 3:
                bag_time_or_shift += correspond_bag[0]
                check_bag = 0
                correspond_bag.clear()
                shift_list.clear()
            elif 3 in shift_list and check_bag == 1:
                bag_time_or_shift += 3
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 2 == correspond_bag[0] or 2 in shift_list and check_bag == 1:
                bag_time_or_shift += 2
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 1 == correspond_bag[0] and check_bag == 1:
                bag_time_or_shift += 1
                correspond_bag.clear()
                shift_list.clear()
                pass
            else:
                correspond_bag.clear()
                shift_list.clear()
                pass
        except IndexError:
            continue

    break                 

print("The amount of delay time was {}".format(bag_time_or_shift * 0.75))
print("The amount of turns required was {}".format(walking_time))
print("The amount of time saved in open space was {}".format(added_time))
print("The amount of time stuck getting to the aisles was {}".format(blocking_aisle))
total_time = walking_time + (round(bag_time_or_shift * 0.75)) + added_time + blocking_aisle
print(total_time)