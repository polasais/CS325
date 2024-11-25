# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325
# Description: This program takes a 2-D puzzle of size MxN, that has N rows and M columns. Each cell is empty or has a
# barrier. Empty cells are marked with '-', whereas barriers are marked with '#'. A starting coordinate as well as a
# destination coordinate are provided, and the shortest path between the two coordinates is to be found.
# The steps should be returned in a list. (The only possible movements are up, down, left, and right).
import heapq


def solve_puzzle(board, source, destination):
    # If the source is the same as the destination, then just return the coordinates as a list.
    if source == destination:
        return [source]

    possible_moves = [(0,1),(1,0),(-1,0),(0,-1)]     # Movements: down, right, up, left.
    width = len(board[0])                            # Returns num of columns in the board
    height = len(board)                              # Returns num of rows in the board
    start_row, start_col = source
    path = [source]                                  # Path keeps track of the current path taken.
    # An empty matrix is created to record if coordinate has been visited.
    visited = [['No'] * width for _ in range(height)]
    heapqueue = [(0, start_row, start_col, path)]    # Min-heap priority queue storing (steps, row, column, cur path)

    while len(heapqueue) > 0:
        cur_steps, cur_row, cur_col, cur_path = heapq.heappop(heapqueue)

        if (cur_row, cur_col) == destination:        # If the destination is reached, then return the path taken.
            return cur_path

        if visited[cur_row][cur_col] == 'Yes':       # If the coordinates have been visited, skip them.
            continue
        visited[cur_row][cur_col] = 'Yes'            # Otherwise, visit them.

        for movement in possible_moves:
            # We check for each movement to see if we should replace the current steps or not.
            new_row, new_col = cur_row + movement[0], cur_col + movement[1]
            # If the new row and columns are in bound, check if there's a barrier.
            if 0 <= new_row < height and 0 <= new_col < width:
                if board[new_row][new_col] != '#':          # If there's no barrier, then check if it has been visited.
                    if visited[new_row][new_col] == 'No':   # If it hasn't been visited, then add it to the cur path.
                        new_path = cur_path + [(new_row, new_col)]
                        heapq.heappush(heapqueue, (cur_steps + 1, new_row, new_col, new_path))
    return



