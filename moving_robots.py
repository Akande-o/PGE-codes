## information is available at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=movingrobots_py
def motion(position, move, command):
    """ Returns the next move based on the current move and the command
    Parameters:
    position - the current position of the robot
    move - the current move of the robot
    command - the command of the robot
    """
    left_dict = {"E": "N", "W": "S", "N": "W", "S": "E"}
    right_dict = {"E": "S", "W": "N", "N": "E", "S": "W"}
    if command == "L":
        move = left_dict[move]
    else:
        move = right_dict[move]
    return move
#initialising some parameters based on the input data available
initial = list(map(int, input().split()))
num_col = initial[0]
num_row = initial[1]
num_steps = initial[2]
move_dict = {0: "E", 1: "N", 2: "W", 3: "S"}     
left_dict = {"E": "N", "W": "S", "N": "W", "S": "E"}
right_dict = {"E": "S", "W": "N", "N": "E", "S": "w"}
bot_1 = list(map(int, input().split()))   # initial position and current direction of the first robot
com_1 = input().split()           # movement sequence of the first robot
mult_1 = num_steps//len(com_1) + 1  # the number of times the sequence must happen
com_1 = com_1 * mult_1     # the required sequence based on the number of cycles
bot_2 = list(map(int, input().split()))  # initial position and current direction of the second robot
com_2 = input().split()         # movement sequence of the second robot
mult_2 = num_steps//len(com_2) + 1  # the number of times the sequence must happen
com_2 = com_2 * mult_2     # the required sequence based on the number of cycles
coord = []
pos_1 = [num_row - bot_1[1] + 1, bot_1[0]]   # the initial position of first robot in the 2d grid
coord.append(pos_1)
pos_2 = [num_row - bot_2[1] + 1, bot_2[0]]  # the initial position of the second robot in the 2d grid
coord.append(pos_2)
move_1 = move_dict[bot_1[2]]     # the next move for the first robot
move_2 = move_dict[bot_2[2]]     # the next move for the second robot
# the process at each step
for i in range(num_steps):
    command_1 = com_1[i]     # the current command 
    # if the command is a direction
    if command_1 == "L" or command_1 == "R":
        move_1 = motion(pos_1, move_1, command_1)
    # the condition the command is a number
    else:
        num = int(command_1)
        # if the current move is North    
        if move_1 == "N":
            for j in range(1, num+1):
                coord_1 = [ pos_1[0] - j , pos_1[1] ]
                # if the destination cell is already occupied or the robot goes outside the grid
                if coord_1 == pos_2 or coord_1[0] < 1:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_1[0]-k, pos_1[1]])
                    pos_1 = [pos_1[0]-j + 1, pos_1[1]]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_1[0]-k, pos_1[1]])
                pos_1 = [pos_1[0] - num , pos_1[1]]
        # if the current move is East
        elif move_1 == "E":
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_1 = [pos_1[0], pos_1[1] + j]
                if coord_1 == pos_2 or coord_1[1] > num_col:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_1[0], pos_1[1] + k])
                    pos_1 = [pos_1[0], pos_1[1] + j - 1]
                    break
            # append each position the robot visits during the movement  
            else:
                for k in range(1,num+1):
                    coord.append([pos_1[0], pos_1[1]+k])
                pos_1 = [pos_1[0] , pos_1[1]+num]
        # if the current move is South
        elif move_1 == "S":
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_1 = [pos_1[0]+j, pos_1[1]]
                if coord_1 == pos_2 or coord_1[0] > num_row:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_1[0]+k, pos_1[1]])
                    pos_1 = [pos_1[0]+j-1, pos_1[1]]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_1[0]+k, pos_1[1]])
                pos_1 = [pos_1[0] + num , pos_1[1]]
        # if the current move is West
        else:
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_1 = [pos_1[0], pos_1[1]-j]
                if coord_1 == pos_2 or coord_1[1] < 1:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_1[0], pos_1[1] - k])
                    pos_1 = [pos_1[0], pos_1[1] - j + 1]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_1[0], pos_1[1]-k])
                pos_1 = [pos_1[0] , pos_1[1] - num]

    # for the second robot   
    command_2 = com_2[i]
    if command_2 == "L" or command_2 == "R":
        move_2 = motion(pos_2, move_2, command_2)
    else:
        num = int(command_2)
        # if the current move is North
        if move_2 == "N":
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_2 = [ pos_2[0] - j , pos_2[1] ]
                if coord_2 == pos_1 or coord_2[0] < 1:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_2[0]-k, pos_2[1]])
                    pos_2 = [pos_2[0]-j + 1, pos_2[1]]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_2[0]-k, pos_2[1]])
                pos_2 = [pos_2[0] - num , pos_2[1]]
        # if the current move is East
        elif move_2 == "E":
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_2 = [pos_2[0], pos_2[1] + j]
                if coord_2 == pos_1 or coord_2[1] > num_col:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_2[0], pos_2[1] + k])
                    pos_2 = [pos_2[0], pos_2[1] + j - 1]
                    break
            # append each position the robot visits during the movement  
            else:
                for k in range(1,num+1):
                    coord.append([pos_2[0], pos_2[1]+k])
                pos_2 = [pos_2[0] , pos_2[1]+num]
        # if the current move is South
        elif move_2 == "S":
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_2 = [pos_2[0]+j, pos_2[1]]
                if coord_2 == pos_1 or coord_2[0] > num_row:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_2[0]+k, pos_2[1]])
                    pos_2 = [pos_2[0]+n-1, pos_2[1]]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_2[0]+k, pos_2[1]])
                pos_2 = [pos_2[0] + num , pos_2[1]]
        # if the current move is West
        else:
            # if the destination cell is already occupied or the robot goes outside the grid
            for j in range(1, num+1):
                coord_2 = [pos_2[0], pos_2[1]-j]
                if coord_2 == pos_1 or coord_2[1] < 1:
                    n = j
                    for k in range(1,n):
                        coord.append([pos_2[0], pos_2[1] - k])
                    pos_2 = [pos_2[0], pos_2[1] - j + 1]
                    break
            # append each position the robot visits during the movement
            else:
                for k in range(1,num+1):
                    coord.append([pos_2[0], pos_2[1]-k])
                pos_2 = [pos_2[0] , pos_2[1] - num]
# we calculate the total number of visited cells in the 2d grid by the robot
number = 0
coord_list = [] 
cells = num_row * num_col               
for position in coord:
    if position not in coord_list:
        coord_list.append(position)
        number += 1
    else:
        number += 0
print(number)

    



