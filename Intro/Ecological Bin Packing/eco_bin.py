# DATA
# first 3 -> bin 1 
# next 3 -> bin 2
# last 3 -> bin 3
# ordered brown, green and clear
# STEPS
# 1) sort bins from data
# 2) set possible color orders
# 3) go throug all the possible orders
# 4) for loops to navigate each bin, and the colors within
# 5) only count moves if the color is not the one chosen for that bin
# 6) update the best option and print it
 


data = list(map(int, input().split()))

bins = [data[0:3], data[3:6], data[6:9]]

colors = ['B', 'G', 'C']

possible_orders = [
    [0,1,2],
    [0,2,1],
    [1,0,2],
    [1,2,0],
    [2,0,1],
    [2,1,0]
]

min_moves = 999999      # big number to ensure moves update properly
best_order = ''         # empty string to save the final output

for i in possible_orders:
    moves = 0
    for bin_idx in range(3):
        for color_idx in range(3):
            if (color_idx != i[bin_idx]):
                moves += bins[bin_idx][color_idx]
    output = colors[i[0]] +  colors[i[1]]  + colors[i[2]]
    if (moves < min_moves) or (moves == min_moves and output < best_order):
        min_moves = moves
        best_order = output

print(f"{best_order} {min_moves}")
