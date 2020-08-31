# Author: Rehoboth Okorie
# Purpose: Plot a usable map of Dartmouth

from cs1lib import *
from load_graph import load_graph  # import the load_graph function; parses text file to create the vertex object
from bfs import bfs  # import the breadth first search function; finds the path between start and goal points

# get the vertices form the text document
dartmouth_graph_dict = load_graph("dart_textxtra.txt")

# load the campus map
dart_map = load_image("dartmouth_map.png")

# set start and goal on the path to be None at first
start, goal = None, None

# sets the mx and my to be zero before a start point is selected; goal is not dependent of mx & my
mx, my = 0, 0

# will contain the info to draw path from start to goal; get the info form the bfs call
path_dict = {}


# function to get mouse click position and saves it to mx, my
def press(mousex, mousey):
    global mx, my  # mx and my will only be updated when the mouse is clicked
    mx, my = mousex, mousey


# called by start graphics
def draw_graph():
    global start, goal, path_dict  # global variables to be updated

    # draws the map onto window
    draw_image(dart_map, 0, 0)
    # set_fill_color(1, 0, 0)
    # draw_circle(381, 779, 8)

    # goes through main dictionary and draws all the edges; drawn before vertices for better aesthetics
    for i in dartmouth_graph_dict:
        dartmouth_graph_dict[i].draw_all_edges()

    # goes through main dictionary
    for z in dartmouth_graph_dict:

        # draws all the vertices
        if dartmouth_graph_dict[z].v_type == "Major":
            dartmouth_graph_dict[z].draw_vertex(8, 0.3, 0.3, 0.5)
        if dartmouth_graph_dict[z].v_type == "Minor":
            dartmouth_graph_dict[z].draw_vertex(8, 0, 1, 0)

        # check if the mouse was clicked in selection range of a vertex
        if dartmouth_graph_dict[z].vert_dist(mx, my) < 8:

            # updates the value of start to the vertex if condition is met
            start = dartmouth_graph_dict[z]
            # draws the name of selected vertex
            start.draw_text(start.name, 8, 0.5, 0, 0.5)

            # draws whatever value is in start in red to show it is selected
            start.draw_vertex(8, 1, 0, 0)

        # resets start and goal to none if the mouse is clicked on a none vertex associated location
        if is_mouse_pressed() and dartmouth_graph_dict[z].vert_dist(mx, my) > 8:
            start, goal = None, None

        if goal is not None:
            if start is not None and goal.vert_dist(mouse_x(), mouse_y()) > 8:
                goal = None

        # checks if the mouse if hovering is range of a vertex; only does this if a start is already selected
        if dartmouth_graph_dict[z].vert_dist(mouse_x(), mouse_y()) < 8 and start is not None and z != start:

            # if both conditions are met, updates gaol to the vertex
            goal = dartmouth_graph_dict[z]

            # draws the name of goal
            goal.draw_text(goal.name, 8, 0.5, 0, 0.5)

            # draws the vertex associated with goal in red
            goal.draw_vertex(8, 1, 0, 0)

            # calls bfs with start as original vertex and goal as target
            path_dict = bfs(start, goal)

        # displays the nodes on the path
        if dartmouth_graph_dict[z] in path_dict and goal is not None:
            dartmouth_graph_dict[z].draw_text(dartmouth_graph_dict[z].name, 8, 0.5, 0, 0.5)

        # iterates through path_dict and draws all the referenced paths and vertices in red
        for j in path_dict:
            if goal is not None:
                # draws the current referenced vertex in red;
                j.draw_vertex(8, 1, 0, 0)

                # draws a path/edge to the vertex that referenced it
                j.draw_edge(path_dict[j], 1, 0, 0)


start_graphics(draw_graph, height=811, width=1012, mouse_press=press)
