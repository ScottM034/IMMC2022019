from random import randint
import random


passenger_list = []
rows = 33
columns = 6
seats = rows * columns
possible_seats = [1, 2, 3]
full_seating = {}
passenger_with_seat = {}
baggage = {}
seating = []
seat_number = {}
total_walk = 0
bag_total_time = 0
total_time = total_walk + bag_total_time
people_and_rows = {"0": 200}
people_and_columns = {}
walking_time = 0
bag_time = 0
people_left = 0
sat_down = []
added_time = 0
total_removed = 0
correspond_bag = []
line_up = []
seat_down_check = []
shift_list = []
bag_time_or_shift = 0
shift = 0
entering_plane = []
block_groupings = [32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
groupings = [1, 2, 3, 6, 5, 4]
shuffled_passengers = []
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
        elif passenger == 198:
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


for x in range(len(block_groupings)):
    for z in range(len(groupings)):
        for i in range(len(passenger_list)):
            if int(people_and_rows.get(passenger_list[i])) == block_groupings[x]:
                if int(people_and_columns.get(passenger_list[i])) == groupings[z]:
                    shuffled_passengers.append(passenger_list[i])
                    print("This person is row {}".format(int(people_and_rows.get(passenger_list[i]))))
                    print("This person is in column {}".format(int(people_and_columns.get(passenger_list[i]))))
                else:
                    pass
            else:
                pass



check_digit = 0
while True:
    while check_digit < seats:
        check_bag = 0
        new_passenger = shuffled_passengers[check_digit]
        entering_plane.insert(0, new_passenger)
        print(entering_plane)
        walking_time += 1
        for i in range(len(entering_plane)):
            if entering_plane.index(entering_plane[(i)]) == int(people_and_rows.get(entering_plane[(i)])):
                    seat_down_check.append(entering_plane[i])
                    line_up.remove(entering_plane[i])
                    for z in range(len(passenger_list)):
                        if int(people_and_rows.get(entering_plane[i])) <= int(people_and_rows.get(passenger_list[z])) and passenger_list.index(entering_plane[i]) > passenger_list.index(passenger_list[z]) :
                            index_difference_calc = passenger_list.index(entering_plane[i]) - passenger_list.index(passenger_list[z])
                            if (int(baggage.get(entering_plane[i]))- index_difference_calc) < 0:
                                pass
                            else:
                                correspond_bag.append((int(baggage.get(entering_plane[i]))) - index_difference_calc)
                            
                        else:
                            pass
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
                                elif int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 4:
                                    shift_list.append(2)
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
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 3:
                                    shift_list.append(4)
                                elif int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 2:
                                    shift_list.append(2)
                                else:
                                    pass
                    if check_digit < (seats - 1):
                        check_digit += 1
                    else:
                        pass
                    new_passenger = shuffled_passengers[check_digit]
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
        correspond_bag.sort(reverse=True)
        print("WHYYYYYYYYYYYYY {}".format(correspond_bag))
        try:
            print("Biggest Bag is {}".format(correspond_bag[0]))
        except IndexError:
            continue
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
            print(entering_plane)
            entering_plane.insert(k, 100)
            walking_time += 1
            for i in range(len(entering_plane)):
                if entering_plane.index(entering_plane[(i)]) == int(people_and_rows.get(entering_plane[(i)])):
                    for x in range(len(entering_plane)):
                         for z in range(len(passenger_list)):
                            if int(people_and_rows.get(entering_plane[i])) <= int(people_and_rows.get(passenger_list[z])) and passenger_list.index(entering_plane[i]) > passenger_list.index(passenger_list[z]) :
                                index_difference_calc = passenger_list.index(entering_plane[i]) - passenger_list.index(passenger_list[z])
                                if (int(baggage.get(entering_plane[i])) - index_difference_calc) < 0:
                                    pass
                                else:
                                    correspond_bag.append((int(baggage.get(entering_plane[i]))) - index_difference_calc)
                            
                            else:
                                pass
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
                                elif int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 4:
                                    shift_list.append(2)
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
                                if int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 3:
                                    shift_list.append(4)
                                elif int(people_and_rows.get(seat_down_check[z])) == person_row and int(people_and_columns.get(seat_down_check[z])) == 2:
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
            correspond_bag.sort(reverse=True)
        try:
            print("Biggest Bag is {}".format(correspond_bag[0]))
        except IndexError:
            continue
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

print("The amount of delay was {}".format(bag_time_or_shift))
print("The amount of turns required was {}".format(walking_time))
print("The amount of time saved in open space was {}".format(added_time))
total_time = walking_time + bag_time_or_shift + added_time
print("Total Time : {}".format(total_time))

   

            










