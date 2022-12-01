import sys

# set up towers A,B,C. the end of the list is the top of the tower

TOTAL_DISKS = 6

# populate Tower A
TOWERS = {'A': list(reversed(range(1, TOTAL_DISKS + 1))),
          'B': [],
          'C': []}


def print_disk(disk_num):
    # print a single disk of width disk_num
    empty_space = ' ' * (TOTAL_DISKS - disk_num)
    if disk_num == 0:
        # just draw the pole
        sys.stdout.write(empty_space + '||' + empty_space)
    else:
        # draw the disk
        disk_space = '@' * disk_num
        disk_num_label = str(disk_num).rjust(2, '_')
        sys.stdout.write(empty_space + disk_space + disk_num_label + disk_space + empty_space)
        

def print_towers():
    # print all three towers
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (TOWERS['A'], TOWERS['B'], TOWERS['C']):
            if level >= len(tower):
                print_disk(0)
            else:
                print_disk(tower[level])
        sys.stdout.write('\n')
    # print the tower labels A,B,C
    empty_space = ' ' * TOTAL_DISKS
    print('%s A%s%s B%s%s C\n' % (empty_space, empty_space, empty_space, empty_space, empty_space))
   
    
def move_one_disk(start_tower, end_tower):
    # move the top disk from start_tower to end_tower
    disk = TOWERS[start_tower].pop()
    TOWERS[end_tower].append(disk)
    
    
def solve(number_of_disks, start_tower, end_tower, temp_tower):
    # move the top number_of_disks from start_tower to end_tower
    if number_of_disks == 1:
        # base case
        move_one_disk(start_tower, end_tower)
        print_towers()
        return
    else:
        # recursive case
        solve(number_of_disks - 1, start_tower, temp_tower, end_tower)
        move_one_disk(start_tower, end_tower)
        solve(number_of_disks - 1, temp_tower, end_tower, start_tower)
        return


# solve
print_towers()
solve(TOTAL_DISKS, 'A', 'B', 'C')

# interactive mode
while True:
    print_towers()
    print('Enter letter of the start tower and the end tower. (A, B, C) or Q to quit.')
    move = input().upper()
    if move == 'Q':
        sys.exit()
    elif move[0] in 'ABC' and move[1] in 'ABC' and move[0] != move[1]:
        move_one_disk(move[0], move[1])
        