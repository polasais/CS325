# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325
import heapq

def minEffort(puzzle):
    width = len(puzzle[0])  # Returns num of columns in the puzzle.
    height = len(puzzle)    # Returns num of rows in the puzzle.
    # Make an empty map which contains all efforts starting from (0,0)
    efforts = [[float('infinity')] * width for _ in range(height)]
    # To move from the first place to the first place is no effort.
    efforts[0][0] = 0
    # Possible movements are up, down, left, and right.
    possible_moves = [(0,1),(1,0),(-1,0),(0,-1)]
    # Min-heap priority queue storing (effort, row, column)
    heapqueue = [(0, 0, 0)]  # We start w/ 0 effort, and at (0,0)
    # While there are items in the heapqueue, which automatically organizes it by smallest = most important.
    while len(heapqueue) > 0:
        cur_effort, cur_row, cur_col = heapq.heappop(heapqueue)
        # If the current effort is greater than the stored effort, skip it.
        if cur_effort > efforts[cur_row][cur_col]:
            continue
        for movement in possible_moves:
            # We check for each movement to see if we should replace the current effort or not.
            new_row, new_col = cur_row + movement[0], cur_col + movement[1]
            # If the new row and columns are in bound, check the diff in weights to see the effort to move there.
            if new_row < height and new_row >= 0:
                if new_col < width and new_col >= 0:
                    weight = abs(puzzle[new_row][new_col] - puzzle[cur_row][cur_col])
                    # The new effort will be the maximum of the current effort or the weight.
                    new_effort = max(cur_effort, weight)
                    # If the new effort is less than the current effort in the efforts list: replace it.
                    if new_effort < efforts[new_row][new_col]:
                        efforts[new_row][new_col] = new_effort
                        heapq.heappush(heapqueue, (new_effort, new_row, new_col))
    return efforts[height - 1][width - 1]