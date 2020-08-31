# Author: Rehoboth Okorie
# Purpose: Write a breadth first search algorithm

import collections

# two lists queue, visited
# two dict backtrace, pertract.
# first vertex passed in (start) will be first in queue, first in first out; out goes into visited
# add adjacent of start if vertex is neither in queue nor in visited
# for back trace, add the vertex as key; its value is a 2 len list of referrer and distance
# when it reaches the target, it add the target and ref and dist to backtrace

# global var points to target, func draws line from target to referee, and start
# next it replaces the var with the former referee and goes into backtrace and gets it info
# repeats until it reaches start

# on the return, it takes the target and using backtrace add to pertract to get the best backwards path


# breadth first search function
def bfs(vertex, target):

    # the queue list holds all vertices that have been reached but not explored from
    queue = [vertex]

    # the visited deque holds all vertices that have been explored form; it's a deck to reduce run time
    # queue can't be a deck because it will mutate during iteration which would throw an error
    visited = collections.deque([])

    # backtrack holds all vertices reached as keys and the values as the vertices the were reached from as values
    # this way the shortest path to the target can be traced back easily
    backtrack = {}

    # start the initial key to be gotten from backtrack when building the path_track
    start = target

    # holds the desired path built from backtrack; makes it easier to just go through dictionary and draw all edges
    path_track = {}

    # iterates through queue; can't use while because it doesn't go well with cs1lib

    for i in queue:

        # gets the adjacent list of the vertex in queue currently being considered and iterates through it
        for j in i.adjacent:

            # checks if the adjacent currently being considered has already been reached or explored from
            if j not in visited and j not in queue:

                # if condition is met adds the adjacent to backtrack with it's referer
                backtrack[j] = i

                # check if the target has been reached; the target would already have been added.txt to backtrack
                # this way, the target is not added.txt to queue and the loop breaks when the target is reached
                if j != target:
                    # if the target hasn't been reached adds all vertices reached to the queue for exploration
                    queue.append(j)

                # breaks the loop if the target is reached by setting queue to empty
                else:
                    queue = []
                # still appends all target explored from to visited
                visited.append(j)

        # check if the original starting vertex has been reached; this way, it stops when the first reference is reached
    while start != vertex:

        # start is initially set to target
        # it adds the start and its value as key and value into path_track maintaining the form from backtrack
        path_track[start] = backtrack[start]

        # sets the start now to the value of the former start and loops
        # this creates a dictionary containing the shortest path to target
        start = backtrack[start]

    # returns path_track
    return path_track
