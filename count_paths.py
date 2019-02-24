"""
Problem:

A frog is jumping in the cooridate plane according to the following rules:
1. From any lattice point (a, b), the frog can jump to (a+1, b), (a, b+1), or (a+1, b+1).
2. There are no right angle turns in the frog's path.

How many different paths can the frog take from (0,0) to (5, 5)?
"""
start_pos = (0, 0)
num_paths = 0
directions = ("right", "up", "diagonal")

def move_to(pos, direction):
    """
    pos: a tuple contains the x, y coordinate
    direction: a direction element in the directions tuple
    returns: a tuple contains the new x, y coordinate after the move
    """
    if direction == "right":
        return (pos[0] + 1, pos[1])
    elif direction == "up":
        return (pos[0], pos[1] + 1)
    else:
        return (pos[0] + 1, pos[1] + 1)

def isEnd(pos, end):
    return pos[0] ==  end[0] and pos[1] == end[1]

def isOut(pos, end): # move outside of plane
    return pos[0] > end[0] or pos[1] > end[1]

def move(from_pos, end_pos, prior_direction):
    """
    A recursive function to move from starting position to the end position, 
    Once it reaches the end position, increase the global num_pathes

    from_pos: a tuple contains the x, y coordinate
    end_pos: a tuple contains the x, y coordinate
    prior_direction: an element in the directions
    """
    for dir in directions:
        # no right angle turns in the path
        if (dir == 'up' and prior_direction == 'right') or (dir == 'right' and prior_direction == 'up'):
            continue
        next_pos = move_to(from_pos, dir)
        if isEnd(next_pos, end_pos):
            global num_paths
            num_paths += 1
        if isOut(from_pos, end_pos):
            continue
        else:
            move(next_pos, end_pos, dir)

def count_paths(end_pos):
    global num_paths
    num_paths = 0
    move(start_pos, end_pos, None)

for i in range(10):
    count_paths((i+1, i+1))
    print(f"{(i+1, i+1)} ==> {num_paths}")
