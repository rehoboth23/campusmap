# AUTHOR: REHOBOTH OKORIE
# PURPOSE: TO CREATE A VERTEX CLASS

from cs1lib import *


class Vertex:

    def __init__(self, name, vetx, vety, adjacent, v_type):
        # name of vertex
        self.name = name
        # list of adjacent vertices
        self.adjacent = adjacent
        # x and y coordinates if vertex on map
        self.vetx = int(vetx)
        self.vety = int(vety)
        self.v_type = v_type
    def __str__(self):
        # string comprehension to build a string from the list of adjacent vertices
        self.adjacent_text = ", ".join(str(i.name) for i in self.adjacent)

        # return a string using string formatting
        return "{0}; Location: {1}, {2}; Adjacent vertices: {3}".format(str(self.name), str(self.vetx), str(self.vety),
                                                                        self.adjacent_text)

    # method that calculates the distance of some values passed in from the center of a vertex
    # will be used to select start and goal vertices
    def vert_dist(self, mx, my):
        dis = ((self.vetx - mx)**2 + (self.vety - my)**2)**0.5
        return dis

    # method to draw a vertex
    def draw_vertex(self, radius, r, g, b):
        # for stroke and sill color, r, g, b control them
        set_stroke_color(r, g, b)
        set_fill_color(r, g, b)
        # draws a vertex represented by a circle with the radius of "radius"
        draw_circle(self.vetx, self.vety, radius)

    # vertex to draw and edge between two vertices
    def draw_edge(self, o_vertex, r=0, g=0, b=0):
        # stoke width is fixed
        set_stroke_width(3)
        # stroke color is controlled by rgb
        set_stroke_color(r, g, b)
        # draws a line from self vertex center to the center of the vertex passed in as o_vertex (other vertex)
        draw_line(self.vetx, self.vety, o_vertex.vetx, o_vertex.vety)

    # vertex to draw all edges of self vertex
    def draw_all_edges(self):
        # goes through self vertex's list of adjacent vertices
        for other in self.adjacent:
            if self.v_type == "Major" and other.v_type == "Major":
                # call draw edge passing the adjacent vertices in as o_vertex; stroke color is set to blue
                self.draw_edge(other, 0, 0, 1)

            else:
                self.draw_edge(other, 1, 0, 1)

    # method that draws vertex name
    def draw_text(self, text, radius, r, g, b):
        # text color is set by rgb
        set_stroke_color(r, g, b)
        # font and font size are fixed
        set_font_size(20)
        set_font("American Typewriter")
        # draws text just above the vertex
        draw_text(text, self.vetx, self.vety - radius)
