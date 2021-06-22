### Information can be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=gallery_py
###  CODE FUNCTIONS
def time_to_min(lst):
    """
    Returns a list of all the times converted to minutes given a list of time in HH:MM format
    Parameters:
    lst - initial list with HH:MM format
    Output:
    time - list of time in minutes
    """
    time = []  # initialised output list
    for start, end in lst:
        s_1 = start.split(":")
        start_min = int(s_1[0]) * 60 + int(s_1[1])   # conversion
        e_1 = end.split(":")
        end_min = int(e_1[0]) * 60 + int(e_1[1])    # conversion
        time.append([start_min, end_min])
    return time
def unclashed_time(lst):
    """
    Prepocesses a list of time (already in minutes) and checks if there is any form of clash between them
    and if there is it attends to it
    Parameters:
    lst - List of times in minutes which may be clashing
    Returns:
    time_lst - List of times which has no clashes
    """
    length = len(lst)      # length of clashing time list
    for i in range(length):
        times = lst[i]
        start = times[0]
        end = times[1]
        # if the both times are the same and are equal to zero
        if start == 0 and end == 0:
            continue
        # we check through the entire list of times and attend to the clashing times
        else:
            for j in range(length):
                start_time = lst[j][0]
                end_time = lst[j][1]
                k = max(i, j)
                l = min(i,j)
                if start_time == 0 and end_time == 0:   # if they are both 0
                    continue 
                elif i == j:             # if it is the same position in the list
                    continue
                elif start < start_time and end > end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start
                    lst[k][1] = end
                elif start < start_time and start_time <= end < end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start
                    lst[k][1] = end_time
                elif start > end_time and end > end_time:
                    continue
                elif start > start_time and  end > end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start_time
                    lst[k][1] = end
                elif start < start_time and end < start_time:
                    continue
                elif start > start_time and start_time < end < end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start_time
                    lst[k][1] = end_time
                elif start == start_time and  start_time < end and end > end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][1] = end
                elif start == start_time and end < end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][1] = end_time
                elif start > start_time and end == end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start_time
                elif start < start_time and end == end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                    lst[k][0] = start
                elif start == start_time and end == end_time:
                    lst[l][0] = 0
                    lst[l][1] = 0
                else:
                    continue
    # initialising the unclashed time list
    time_lst = []
    # cleaning up the clashed time data
    for st, et in lst:
        if st == et == 0:
            continue
        else:
            time_lst.append([st, et])
    return time_lst

def free_time(lst):
    """
    Returns the total free time within 10 hours of a working day given a list of times which the guards were available 
    """
    minute = 0
    for st, et in lst:
        minute += et -st + 1     # summing up the total number of minutes
    free_time = 600 - minute
    free_h = str(free_time//60)
    free_m = str(free_time % 60)
    # converting the free time to HH:MM format
    return (2 - len(free_h)) * "0" + free_h + ":" + (2 - len(free_m))*"0" + free_m
###  END OF CODE FUNCTIONS

# initialising the parameters based on the input data
initial = list(map(int, input().split(", ")))
num_per = initial[0]
num_steps = initial[1]
persons = input().split(", ")      # list of the guards
person_1 = {}                    # initialising the dictionary of times of each person in hall 1
person_2 = {}                    # initialising the dictionary of times of each person in hall 2
person_dict = {}                 # initialising the dictionary of the total time each person spent in both halls
for person in persons:
    person_1[person] = []
    person_2[person] = []
    person_dict[person] = 0
gallery = input().split(", ")  # the two galleries or halls
hall_1 = gallery[0]
hall_2 = gallery[1]
for num in range(num_steps):
    # getting some data based on the information provided by the input data
    line = input().split(", ")
    name = line[0]
    start = line[1]
    end = line[2]
    hall = line[3]
    if hall == hall_1:
        person_1[name].append([start, end])
    else:
        person_2[name].append([start, end])
# the total time for each guard 
for person in persons:
    human_1 = person_1[person]      # getting the list of times in hall 1
    human_2 = person_2[person]      # getting the list of times in hall 2
    time_1 = time_to_min(human_1)  # using a predefined function to convert time from HH:MM format to minutes in hall 1    
    time_2 = time_to_min(human_2)  # using a predefined function to convert time from HH:MM format to minutes in hall 2
    clash_1 = unclashed_time(time_1) # using a predefined function to deal with the time clashes in hall 1
    clash_2 = unclashed_time(time_2) # using a predefined function to deal with the time clashes in hall 2
    minutes = 0
    # Now, we're trying to get the conflict time for each guard in both halls
    for s_min1, e_min1 in clash_1:
        # we basically compare the two times in the halls and find the total time the guards are in both halls
        for s_min2, e_min2 in clash_2:
            if s_min1 < s_min2 and e_min1 > e_min2:
                minutes += e_min2 - s_min2 + 1
            elif s_min1 < s_min2 and e_min1 < s_min2:
                minutes += 0
            elif s_min1 <= s_min2 and s_min2<=e_min1 <= e_min2:
                minutes += e_min1 - s_min2 + 1
            elif s_min1 > e_min2 and e_min1 > e_min2:
                minutes += 0
            elif s_min1 >= s_min2 and  s_min2 <= e_min1 and e_min1 >= e_min2:
                minutes += e_min2 - s_min1 + 1
            elif s_min1 >= s_min2 and s_min2<=e_min1 <= e_min2:
                minutes += e_min1 - s_min1 + 1
            else:
                minutes += 0
    person_dict[person] = minutes   # attributing the total clash minutes as values to the corresponding guard
# sorting the data so it's in alphabetical order
new_list = sorted(person_dict)
new_dict = {}
for i in new_list:
    new_dict[i] = person_dict[i]
sort_time = sorted(new_dict, key = new_dict.get)


first_hall = []
second_hall = []
# getting all the time data for both halls regardless of the guards on duty
for times_1 in person_1.values():
    first_hall += times_1
for times_2 in person_2.values():
    second_hall += times_2
first_time = time_to_min(first_hall)  # using a predefined function to convert time from HH:MM format to minutes in hall 1
second_time = time_to_min(second_hall) # using a predefined function to convert time from HH:MM format to minutes in hall 2
first_clash = unclashed_time(first_time) # using a predefined function to deal with the time clashes in hall 1
second_clash = unclashed_time(second_time) # using a predefined function to deal with the time clashes in hall 2
first_free = free_time(first_clash)   # using a predefined function to calculate the free time in hall 1
second_free = free_time(second_clash) # using a predefined function to calculate the free time in hall 2
print(first_free, second_free)
for name in sort_time:
    clash = person_dict[name] 
    clash_h = str(clash//60)
    clash_m = str(clash%60)
    clash_time = (2 - len(clash_h)) * "0" + clash_h + ":" + (2 - len(clash_m))*"0" + clash_m
    print(clash_time, name)

