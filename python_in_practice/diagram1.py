import os
import sys
import tempfile


def main():
    # print(len(sys.argv), sys.argv[0])
    if len(sys.argv) > 1 and sys.argv[1] == '-P':


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)


class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)


BLANK = ' '
CORNER = '+'
HORIZONTAL = '-'
VERTICAL = '|'


class Diagram:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.diagram = _create_rectangle(self.width, self.height, BLANK)


def _create_rectangle(width, height, fill):
    

if __name__ == '__main__':
    main()
