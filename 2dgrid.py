## information available at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=gridbuilding_py

# initialising some parameters based on the input data available
initial = list(map(int, input().split()))
num_rows = initial[0]
num_col = initial[1]
num_steps = initial[2]
rows = []        # the list of rows
cols = []        # the list of columns
num = 0
# The process at each step
for i in range(num_steps):
    line = input().split()    # reading the input line
    row = int(line[1])
    col = int(line[2])
    # the condition of it being a put statement 
    if line[0] == "P":
        size = int(line[3])    # this case it will involve the size of the 2d array
        # if the array does not go outside of the initially defined 2d grid
        if row + size - 1 <= num_rows-1 and col + size -1 <= num_col-1:
            range_row = [row, row+size-1]
            range_col = [col, col+size-1]
            # if there is already a 2d array within the grid
            if len(rows) !=0 and len(cols)!=0:
                j = len(rows)
                # check if the new 2d array and any other previously existing 2d array would take the same row and column
                for i in range(j):
                    for k in range(size):
                        for l in range(size):
                            if rows[i][0]<=row+k<=rows[i][1] and cols[i][0]<=col+l<=cols[i][1]:
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                # if there is no clash between any previously existing 2d array and the current one then we add the array
                else:
                    rows.append(range_row)
                    cols.append(range_col)
                    num += size*size
            # the condition of there being no previously existing 2d array within the 2d grid 
            else:
                rows.append(range_row)
                cols.append(range_col)
                num += size*size
        else:
            continue
    # if it is a move "M" command 
    else:
        move = line[3]     # we're dealing with the directions in this case
        numb = len(rows)
        # we check through the entire grid for the 2d array which has an element in the position
        for i in range(numb):
            if rows[i][0]<=row<=rows[i][1] and cols[i][0]<=col<=cols[i][1]:
                size = rows[i][1] - rows[i][0] + 1
                index = i
                # the condition we have to move the array north or up
                if move == "N":
                    for j in range(numb):
                        if rows[j][0] == rows[j][1] and cols[j][0] == cols[j][1]:
                            if rows[index][0]-1 == rows[j][0]:
                                break
                        else:
                            for k in range(size):
                                if rows[j][0]<=rows[index][0]-1<=rows[j][1] and cols[j][0]<=col+k<=cols[j][1]:
                                    "break both loops"
                    else:
                        if rows[index][0]-1 < 0:
                            continue
                        else:
                            rows[index][0]-=1
                            rows[index][1]-=1
                # the condition of moving the array west or left
                elif move == "W":
                    for j in range(numb):
                        if rows[j][0] == rows[j][1] and cols[j][0] == cols[j][1]:
                            if cols[index][0]-1 == cols[j][0]:
                                break
                        else:
                            for k in range(size):
                                if rows[j][0]<=row + k<=rows[j][1] and cols[j][0]<=cols[index][0]-1<=cols[j][1]:
                                    "break both loops"
                    else:
                        if cols[index][0]-1 < 0:
                            continue
                        else:
                            cols[index][0]-=1
                            cols[index][1]-=1
                # the condition we have to move the array south or down
                elif move == "S":
                    for j in range(numb):
                        if rows[j][0] == rows[j][1] and cols[j][0] == cols[j][1]:
                            if rows[index][1]+1 == rows[j][1]:
                                break
                        else:
                            for k in range(size):
                                if rows[j][0]<=rows[index][1]+1<=rows[j][1] and cols[j][0]<=col+k<=cols[j][1]:
                                    "break both loops"
                    else:
                        if rows[index][1]+1 > num_rows -1:
                            continue
                        else:
                            rows[index][0]+=1
                            rows[index][1]+=1
                # the condition we have to move the array east or right
                else:
                    for j in range(numb):
                        if rows[j][0] == rows[j][1] and cols[j][0] == cols[j][1]:
                            if cols[index][1]+1 == cols[j][1]:
                                break
                        else:
                            for k in range(size):
                                if rows[j][0]<=row + k<=rows[j][1] and cols[j][0]<=cols[index][1]+1<=cols[j][1]:
                                    "break both loops"
                    else:
                        if cols[index][1]+1 > num_col -1:
                            continue
                        else:
                            cols[index][0]+=1
                            cols[index][1]+=1
        else:
            continue
# we compute the total number of free cells
free = num_col*num_rows - num
print(free)
        
