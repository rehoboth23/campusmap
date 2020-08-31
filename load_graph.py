# Author: Rehoboth Okorie
# Purpose: Get the mapping info of Dartmouth college

from vertex import Vertex


# parses the line into a form that can be sent into a call for a Vertex class
def parse_line(line):
    # splits up the lines at the semi-colons and save it to split_line
    split_line = line.strip().split(";")

    # gets the vertex name from the first index of slit_line
    vertex_name = split_line[0].strip()

    # gets the list of adjacent vertices form split_line index 1 and splits it at the commas
    adjacent_vertices = split_line[1].strip().split(",")
    adjacent = []

    # iterates through adjacent_vertices and adds the adjacent to list adjacent
    for i in adjacent_vertices:
        adjacent.append(i.strip())

    # splits the coordinates of the vertex at the commas and saves it to coordinates
    coordinates = split_line[2].strip().split(",")

    # gets the coordinates in turn and saves them to vetx and vety
    vetx, vety = coordinates[0].strip(), coordinates[1].strip()

    # get the vertex type
    v_type = split_line[3].strip()

    # returns vertex name, list of adjacent, x position and y position
    return vertex_name, adjacent, vetx, vety, v_type


# will load the file; create the vertex objects; creates a dictionary of vertex objects from the loaded file
def load_graph(file):

    # creates an empty dictionary
    vert_dict = {}

    # loads file into infile
    infile = open(file, "r")

    # goes through every line in infile
    for line in infile:

        # checks if when split at semi-colons, it can be passes into parse_line
        if len(line.split(";")) == 4:

            # passes line into parse_line and saves values vertex_name, adjacent, vetx, vety
            vertex_name, adjacent, vetx, vety, v_type = parse_line(line)

            # creates a vertex object using our values; add the object to vert_dict with the key as vertex_name
            # adjacent is originally set to an empty list
            vert_dict[vertex_name] = Vertex(vertex_name, vetx, vety, [], v_type)

    # close file
    infile.close()

    # reopens file
    infile = open(file, "r")

    # goes through each line in file again
    for line in infile:

        # next two steps same as in first iteration
        if len(line.split(";")) == 4:
            vertex_name, adjacent, vetx, vety, v_type = parse_line(line)

            # goes through the list of it's adjacent names
            for i in adjacent:

                # appends the vertex associated with adjacent name to self's adjacent list
                # creates a list of adjacent vertices and not adjacent names
                vert_dict[vertex_name].adjacent.append(vert_dict[i])

    # close file
    infile.close()

    # return the dictionary of vertex objects
    return vert_dict
