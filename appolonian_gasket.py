### Information can be found at https://cw.felk.cvut.cz/brute/data/ae/release/2021l_be5b33pge/pge2021/evaluation/input.php?task=apolloniangasket
import math
# We're trying to find the area and perimeter of all circles in appolonian gasket given the initial two diameters and minimum diameter
# CODE FUNCTIONS
def first_area_set(D1, D2, D_outer, min_D):
    """Returns the total area of the circles in an appolonian gasket given the two initial diameters 
    and the minimum diameter by creating the first set which involves the outermost circle with negative curvature, the
    larger of the initial small circle and the newly generated circle
    Parameters:
    D1 - one of the two circles with initial diameters given
    D2 - one of the two circles with initial diameters given
    D_outer - the sum of D1 and D2 but with negative curvature
    min_D - the minimum diameter allowed in the appolonian gasket
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D_outer
    b = 1/D1
    c = 1/D2
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5  # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5  # the second possibiliy using the theorem
    D = min(abs(1/d1), abs(1/d2))  # the newly generated circle 
    if D > min_D:
        Area = 2*math.pi*(D**2)   #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + first_area_set(D, D2, D_outer, min_D) + second_area_set(D1, D2, D, min_D) + third_area_set(D1, D, D_outer, min_D)
def second_area_set(D1, D2, D3, min_D):
    """Returns the total area of circles within an appolonian gasket which involves the three circles
    with positive curvature after using the first set to generate the first set of circles
    Parameters:
    D1, D2, D3- The three circles which have positive curvature while creating the first set usually involves one of 
    the two initially given circles and while it keeps reducing it may use the current circle as well
    min_D - The minimum diameter
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D or D3 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D1
    b = 1/D2
    c = 1/D3
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5  # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5  # the second possibility using the theorem
    D = min(abs(1/d1), abs(1/d2))        # the newly generated circle
    if D > min_D:
        Area = 2*math.pi*(D**2)       #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + second_area_set(D1, D, D3, min_D) + second_area_set(D1, D2, D, min_D) + second_area_set(D, D2, D3, min_D)
def third_area_set(D1, D2, D_outer, min_D):
    """Returns the total area of the third set of circles in an appolonian gasket while computing the first set. It 
    usually involves the outermost circle with negative curvature. the smaller of the two initially defined circles
    and the newly generated circle
    D1, D2 - The circles with positive curvature
    D_outer - The outermost circle with negative curvature
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D_outer
    b = 1/D1
    c = 1/D2
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5   # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5   # the second possibility using the theorem
    D = min(abs(1/d1), abs(1/d2))     # the newly generated circle
    if D > min_D:
        Area = 2*math.pi*(D**2)      #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + third_area_set(D1, D, D_outer, min_D) + third_area_set(D, D2, D_outer, min_D) + second_area_set(D1, D2, D, min_D)

def first_set(D1, D2, D_outer, min_D):
    """Returns the total perimeter of the circles in an appolonian gasket given the two initial diameters 
    and the minimum diameter by creating the first set which involves the outermost circle with negative curvature, the
    larger of the initial small circle and the newly generated circle
    Parameters:
    D1 - one of the two circles with initial diameters given
    D2 - one of the two circles with initial diameters given
    D_outer - the sum of D1 and D2 but with negative curvature
    min_D - the minimum diameter allowed in the appolonian gasket
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D_outer
    b = 1/D1
    c = 1/D2
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5     # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5     # the second possibility using the theorem
    D = min(abs(1/d1), abs(1/d2))                 # the newly generated circle
    if D > min_D:
        Area = 4*math.pi*(D)                     #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + first_set(D, D2, D_outer, min_D) + second_set(D1, D2, D, min_D) + third_set(D1, D, D_outer, min_D)
def second_set(D1, D2, D3, min_D):
    """Returns the total area of circles within an appolonian gasket which involves the three circles
    with positive curvature after using the first set to generate the first set of circles
    Parameters:
    D1, D2, D3- The three circles which have positive curvature while creating the first set usually involves one of 
    the two initially given circles and while it keeps reducing it may use the current circle as well
    min_D - The minimum diameter
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D or D3 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D1
    b = 1/D2
    c = 1/D3
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5      # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5      # the second possibility using the theorem
    D = min(abs(1/d1), abs(1/d2))              # the newly generated circle
    if D > min_D:
        Area = 4*math.pi*(D)                  #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + second_set(D1, D, D3, min_D) + second_set(D1, D2, D, min_D) + second_set(D, D2, D3, min_D)
def third_set(D1, D2, D_outer, min_D):
    """Returns the total area of the third set of circles in an appolonian gasket while computing the first set. It 
    usually involves the outermost circle with negative curvature. the smaller of the two initially defined circles
    and the newly generated circle
    D1, D2 - The circles with positive curvature
    D_outer - The outermost circle with negative curvature
    """
    # if the minimum has been reached
    if D1 < min_D or D2 < min_D:
        return 0
    # computing the curvature for DesCartes' Theorem
    a = 1/D_outer
    b = 1/D1
    c = 1/D2
    d1 = a + b + c + 2*(a*c + b*c + a*b)**0.5      # the first possibility using the theorem
    d2 = a + b + c - 2*(a*c + b*c + a*b)**0.5      # the second possibility using the theorem
    D = min(abs(1/d1), abs(1/d2))                  # the newly generated circle
    if D > min_D:
        Area = 4*math.pi*(D)                      #if it is greater than the minimum allowed both up and down
    else:
        Area = 0
    return Area + third_set(D1, D, D_outer, min_D) + third_set(D, D2, D_outer, min_D) + second_set(D1, D2, D, min_D)
# converting the string to 3 decimal places
def string_3d(string):
    real, frac = string.split(".")
    frac = frac + "0"*(3 - len(frac))
    return real + "." + frac
###  END OF CODE FUNCTIONS

# Initialising some parameters based on the input data
initial = list(map(float, input().split()))
d1, d2, min_d = initial
d_1 = min(d1, d2)
d_2 = max(d1, d2)
r_outer = -(d1 + d2)/2  # this is because of the negative curvature
r1 = d_1/2
r2 = d_2/2
min_r = min_d/2
# computing the total area and perimeter of the circles
area , circumference = math.pi*(r1**2 + r2**2) + first_area_set(r1, r2, r_outer, min_r), 2*math.pi*(r1 + r2) + first_set(r1, r2, r_outer, min_r)
str_area = str(round(area, 3))
str_per = str(round(circumference, 3))
print(string_3d(str_area), string_3d(str_per))