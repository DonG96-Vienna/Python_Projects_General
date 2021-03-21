import math

lst_x_y = []
with open('x_y_csv.txt') as f:
    for line in f:
        lst_x_y.append([int(n) for n in line.strip().split(',')])


dist_all = []

# Distanz zwischen benachbarten Punkten finden
for i in range(0, len(lst_x_y) - 1):
    dist = math.sqrt((lst_x_y[i+1][0] - lst_x_y[i][0])**2 + (lst_x_y[i+1][1] - lst_x_y[i][1])**2)

    dist_all.append(dist)

print(dist_all)