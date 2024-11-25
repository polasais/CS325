# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325
# Source: Exploration 4.4 Canvas CS325.

def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    return result

def powerset_helper(pointer, choices_made, inputSet, result):
    if pointer < 0:      # If the pointer is negative, append a copy of the choices made to results.
        result.append(choices_made.copy())
        return

    choices_made.append(inputSet[pointer])
    powerset_helper(pointer-1, choices_made, inputSet, result)
    #backtracking
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, inputSet, result)
