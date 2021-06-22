### information could be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=rectanglesarea
# initialise the 2d array and the number of rows and columns
arr = []
M, N = list(map(int, input().split()))
# getting together the array from the proposed input data
for i in range(M):
    line = list(map(int, input().split()))
    arr.append(line)
range_rows = []
# implementing a for loop in such a way that we can get the columns of 1s in each row
for n, lst in enumerate(arr):
    start = 0
    end = 0
    for i in range(N):
        if lst[i] == 1 and end == 0:
            start = i
            end = i+1
        elif lst[i] == 1 and end != 0 and i == N-1:
            range_rows.append((n, start, end))
        elif lst[i] == 1 and end!= 0:
            end += 1
        elif lst[i] == 0 and end == 0:
            end = 0
            start = 0
        elif lst[i] == 0 and end != 0:
            end -= 1
            range_rows.append((n, start, end))
            end = 0
            start = 0
# sort the rows according to the second and third element in the tuple 
range_rows = sorted(range_rows, key = lambda element: (element[1], element[2]))
# check for possible rectangles within the 2d array by checking if the initial and final column numbers are the same
poss_rect = []
for i in range(len(range_rows)- 1):
    if range_rows[i][1] == range_rows[i+1][1] and range_rows[i][2] == range_rows[i+1][2] and (range_rows[i][2]- range_rows[i][1]) > 1:
        poss_rect.append((range_rows[i], range_rows[i+1]))
    else:
        continue
# check for the already defined possible rectangles if the sides are all 1s
rect = []
for points in poss_rect:
    first, second = points
    for i in range(first[0], second[0]):
        if arr[i][first[1]] != arr[i][second[1]] or  arr[i][first[2]] != arr[i][second[2]]:
            break
        elif arr[i][first[1]] == arr[i][second[1]] == 0 or arr[i][first[2]] == arr[i][second[2]]== 0:
            break
    else:
        rect.append(points)
# if the sides are all 1s we compute the number of complete rectangles in the array and the total number of 0s in complete rectangles
area = 0
for values in rect:
    top, bottom = values
    area += (bottom[0]-top[0]-1)*(top[2]-top[1]-1)
print(len(rect), area)
