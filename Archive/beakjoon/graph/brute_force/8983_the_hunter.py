import sys

init_data = list(map(int, sys.stdin.readline().split()))
fs_num, ani_num, firing_range = init_data[0], init_data[1], init_data[2]

firing_spots = list(map(int, sys.stdin.readline().split()))

animal_num = [list(map(int, sys.stdin.readline().split())) for _ in range(ani_num)]

cnt = 0
killed_already = []
for firing_spot in firing_spots:
    in_range = []
    x_len = firing_range
    for i in range(firing_range):
        for j in range(firing_spot - (x_len-1), firing_spot + x_len):
            in_range.append([j, i + 1])
        x_len -= 1
    for animal_loc in animal_num:
        if animal_loc not in killed_already:
            for fire_able in in_range:
                if animal_loc == fire_able:
                    killed_already.append(animal_loc)
                    cnt += 1

print(cnt)