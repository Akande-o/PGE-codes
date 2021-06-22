### In formation can be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=scoretable_py

##    CODE FUNCTIONS
def initial_teams(lst):
    """ Returns a 2d array given a list given the list of teams we're considering
    Parameters:
    lst - List of teams in the score table
    Output:
    array - 2d array of dimensions (len(lst) + 1)**2 with each cell a space of 8 
    """
    n = len(lst)
    array = [["     0:0"] *(n+1) for i in range(n+1)]
    for j in range(n):
        array[j + 1][0] = (8 - len(lst[j])) * " " + lst[j]
        array[0][j+1] = (8 - len(lst[j])) * " " + lst[j]
        array[0][0] = 8* " "
        array[j+1][j+1] = 8* " "
    return array
def score(lst):
    """ Returns a score given a list of string characters with a semicolon between them
    """
    score_list = []     # initialising the list of scores
    for score in lst:
        scores = score.split(":")
        if len(scores) != 2:   # if it is more than 2 then we skip
            continue
        i, j = scores[0], scores[1]
        # check if it is a numerical number and is between 0 and 20
        if i.isdecimal() and j.isdecimal():
            if 0<= int(i) <= 20 and 0<= int(j) <= 20:
                score_list.append(score)
    # since there can only be one score per line 
    if len(score_list) > 1:
        return None
    # the condition there is no score in the lin at all
    elif len(score_list) == 0:
        return None
    return score_list[0]
def add_scores(string_1, string_2):
    """Returns the string of the total score between two teams with two matches
    Parameters:
    String_1 - the first string of score numbers
    string_2 - the second string of score numbers
    Output:
    score - sum of the two strings
    """
    list_1 = string_1.split(":")
    list_2 = string_2.split(":")
    score = str(int(list_1[0]) + int(list_2[0])) + ":" + str(int(list_1[1]) + int(list_2[1]))
    return score
##   END OF CODE FUNCTIONS
# Initialising some parameters based on the input data
teams = sorted(input().split())
output_teams = initial_teams(teams)
num_teams = int(input())
# We check through each line for two teams and scores
for i in range(num_teams):
    line = input().split()
    line_team = [x for x in line if x in teams]  # teams in the line
    # since we can only have two teams in a match
    if len(line_team) != 2:
        continue
    check_score = [x for x in line if ":" in x]  # checking for strings which could be score numbers 
    scores = score(check_score)    # using a predefined function to get the score in the line
    if scores is None:
        continue
    # we add the scores to the current score within the initially defined 2d array
    team_1 = line_team[0]
    team_2 = line_team[1]
    j = teams.index(team_1) + 1  # getting the index for the first team
    k = teams.index(team_2) + 1  # getting the index for the second team
    current_score = add_scores(output_teams[j][k], scores)  # getting the new score
    output_teams[j][k] = (8-len(current_score))*" " +current_score # maintaining the space of 8 characters in each cell
    # Doing the last 5 steps for the reverse cell
    scorem = scores.split(":")
    scored = reversed(scorem)
    new_score = ":".join(scored)
    also_score = add_scores(output_teams[k][j], new_score)
    output_teams[k][j] = (8-len(also_score))* " " + also_score
# printing the output score table
for line in output_teams:
    print("".join(line)) 