# Name: Isac Polasak
# OSU Email: Polasais@oregonstate.edu
# Course: CS325
# Description: The code implements Prim's Algorithm to find the Minimum Spanning Tree (MST) of a given graph 
# represented as an adjacency matrix G. It starts from a chosen node (index 0), maintains a list of visited 
# nodes and possible edges, and iteratively selects the smallest edge connecting a visited node to an unvisited node.


def Prims(G):
    MST = []
    starting_node = 0
    # The set of nodes we visited:
    visited = [starting_node]
    possible_edges = []

    for column in range(len(G[starting_node])):
        weight = G[starting_node][column]
        if weight != 0:
            # If there's an edge, add it to possible edges along with the weight.
            possible_edges.append((weight, starting_node, column))
            # Now each edge in possible edges will be the weight, the origin node (which vertex the edge starts from),
            # and the column (which vertex the edge ends in)

        # While not all nodes have been visited yet, continue looping to add all nodes to the visited list.

    while len(visited) < len(G):
        # After adding all possible edges, sort it to have lowest weight first.
        possible_edges.sort()
        # For each edge, extract the weight, the origin vertex and the destination vertex:
        for edge in possible_edges:
            weight, from_vertex, to_vertex = edge
            # Now check if the origin vertex is in the visited and the destination is not in visited,
            # if so you can add it, otherwise check for the next edge.
            if from_vertex in visited and to_vertex not in visited:
                MST.append((from_vertex, to_vertex, weight))
                visited.append(to_vertex)
                # After it has been added, add the edges from the new "origin" (aka the vertex we just visited),

                # If from the new vertex, there is an item with weight and it's not been visited, add it
                # the list of possible edges.
                for column in range(len(G[to_vertex])):
                    next_weight = G[to_vertex][column]
                    if next_weight != 0 and column not in visited:
                        possible_edges.append((next_weight, to_vertex, column))
                # and remove the edge from possible edges since it has been used.
                possible_edges.remove(edge)
                break  # Break the loop after adding the edges to MST
    return MST
