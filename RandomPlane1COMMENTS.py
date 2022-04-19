from random import randint
import random
#This code was the base of every other code, it began as everyone being assigned a random seat and going to them in a random order
#This meant i had to import the random functions

passenger_list = [] #list of all passengers on the plane in no particular order
rows = 33  #variable that would change per plane dependent on rows
columns = 6 #variable that would change per plane dependent on the amount of seats in one row
seats = rows * columns #Total number of seats calculated by the other two variables
baggage = {} #The randomly assigned baggage variable to each passenger
people_and_rows = {"0": 200} #Dictionary with each passenger and the row they are in, the starting block is a random constant used to fill space
people_and_columns = {} #Dictionary with each passenger and the seat they are in on a row
walking_time = 0 #The amount of turns(defined in main doc) that occurs to fill the plane
bag_time = 0 #The amount of time taken due to people blocking the aisle due to baggage
sat_down = [] #A variable that would keep track of if multiple passengers sat down at the same time
added_time = 0 #The amount of time saved due to multiple passengers sitting at the same time
correspond_bag = [] #The list used to see what bags were being put away during each turn
seat_down_check = [] #Used to check if someone was in the way of a passenger's seat
shift_list = [] #List that kept track of everyone that had to shift during a specific turn
bag_time_or_shift = 0 #Keeps track of the total time spent shifting seats or blocking the aisle due to baggage
entering_plane = [] #The main list that kept track of everyone in the plane at any given time


ranges = [[0], [1, 2, 3, 4], [5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33, 34, 35]]
ranges_probability = [40, 14, 23, 23, 19, 12, 7, 2]
all_probs = []
#These were the found probabilities for the time taken for someone to put away a single bag



for i in range(len(ranges)):
    for x in range(len(ranges[i])):
        for z in range(ranges_probability[i]):
            all_probs.append(ranges[i][x])

#Creates a list with the given probabilities to be added to baggage later
    


#Randomising seat order
while len(passenger_list) != (seats):
    for i in range(seats):
        passenger = randint(0, (seats))
        if passenger in passenger_list:
            pass
        elif passenger == 198:
            pass
        else:
            passenger_list.append(passenger)


#Giving each person a row            
for i in range(rows):
    for j in range(columns):
        row_seat_check = (columns * i) + j
        people_and_rows[row_seat_check] = i
for i in range(rows):
    if i in people_and_rows:
        pass
    else:
        people_and_rows.append(i)


        
    
#Giving each person a seat in their row
for i in range(rows):
    for j in range(columns):
        column_seat_check = (columns * i) + j
        people_and_columns[column_seat_check] = (j + 1)


#Giving each person a random bag time to put away
for i in range(seats):
        baggage[i] = random.choice(all_probs)

#ONLY USED FOR Q 2B, causing a person to not follow the method and moving them forward in the line
#Does not affect this specific code as this is already random to begin with
for i in range(round(0.05 * seats)):
    not_following = randint(1, len(passenger_list))
    while True:
        random_position = randint(1, (len(passenger_list) - 1))
        if random_position < not_following:
            pass
        else:
            break

dude_taken = passenger_list[not_following]
passenger_list.remove(passenger_list[not_following])
passenger_list.insert(random_position, dude_taken)


#Main Loop 
check_digit = 0 #The check digit checks if everyone has entered the plane, thus as to start adding place holders to push passengers forward
while True:
    while check_digit < seats: 
        new_passenger = passenger_list[check_digit] #Defines a new passenger into the plane from the line
        entering_plane.insert(0, new_passenger) #Adds that passenger
        print(entering_plane)
        walking_time += 1 #The turn increment counter, adds whenever someone causes the plane to move forward a step
        for i in range(len(entering_plane)): #For every person on the plane check if they can sit down
            if entering_plane.index(entering_plane[(i)]) == int(people_and_rows.get(entering_plane[(i)])): 
                    seat_down_check.append(entering_plane[i]) #If they can sit down, add the amount of time spent putting away the bag, put into parallels with others and add the largest
                    for z in range(len(passenger_list)):
                        if int(people_and_rows.get(entering_plane[i])) <= int(people_and_rows.get(passenger_list[z])) and passenger_list.index(entering_plane[i]) > passenger_list.index(passenger_list[z]) :
                            index_difference_calc = passenger_list.index(entering_plane[i]) - passenger_list.index(passenger_list[z])
                            if (int(baggage.get(entering_plane[i]))- index_difference_calc) < 0:
                                pass
                            else:
                                correspond_bag.append((int(baggage.get(entering_plane[i]))) - index_difference_calc)
                            
                        else:
                            pass
                    sat_down.insert(0, (entering_plane[(i)])) #Keep track of who has sat down
                    person_row = int(people_and_rows.get(entering_plane[(i)]))
                    person_column = int(people_and_columns.get(entering_plane[i]))
                    if person_column > 3: #Check if a person is already sitting in that row and in the way of the new person's seat
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
                    new_passenger = passenger_list[check_digit]
            elif entering_plane.index(entering_plane[(i)]) != int(people_and_rows.get(entering_plane[(i)])):
                pass #If everyone on the plane can't sit down, add somoene new and push everyone forward 1
        while True:
            if len(sat_down) != 0:
                entering_plane.remove(sat_down[0])
                sat_down.remove(sat_down[0])
                added_time -= 1 #If there are multiple people sitting at one time, time is saved, thus minus in this counter
            else:
                break
        if check_digit <= (seats - 1):
            check_digit += 1 #Checks if adding more to the check_digit would cause it to create a index error
        else:
            pass
        correspond_bag.sort(reverse=True)
        try: #Add the largest bag amount for every turn taken if there are parallels as it would block the line
            if correspond_bag[0] > 3: 
                bag_time_or_shift += correspond_bag[0]
                correspond_bag.clear()
                shift_list.clear()
            elif 3 in shift_list:
                bag_time_or_shift += 3
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 2 == correspond_bag[0] or 2 in shift_list:
                bag_time_or_shift += 2
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 1 == correspond_bag[0]:
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
    while check_digit == seats: #Once nearly everyone has sat down, placeholders are added in this loop to continue to push everyone forward
        for k in range(rows):
            print(entering_plane)
            entering_plane.insert(k, 100) #Placeholder as to not cause index errors, or non-real errors
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
                else:
                    break
            check_digit += 1 
            correspond_bag.sort(reverse=True)
        try:
            if correspond_bag[0] > 3:
                bag_time_or_shift += correspond_bag[0]
                correspond_bag.clear()
                shift_list.clear()
            elif 3 in shift_list:
                bag_time_or_shift += 3
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 2 == correspond_bag[0] or 2 in shift_list:
                bag_time_or_shift += 2
                correspond_bag.clear()
                shift_list.clear()
                pass
            elif 1 == correspond_bag[0]:
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
total_time = walking_time + bag_time_or_shift + added_time #Final time calculation given all the previous variables
print("Total Time : {}".format(total_time))

   

            










