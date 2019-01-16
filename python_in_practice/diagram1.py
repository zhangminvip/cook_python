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

    def make_rectangle(self, x, y, width, height, fill='white',
                       stroke='black'):
        return Rectangle(x, y, width, height, fill, stroke)





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
    rows = [[fill for _ in range(width)] for _ in range(height)]
    for x in range(1, width -1):
        rows[0][x] = HORIZONTAL
        rows[height - 1][x] = HORIZONTAL
    for y in range(1, height - 1):
        rows[y][0] = VERTICAL
        rows[y][width - 1] = VERTICAL
    for y, x in (0, 0), (0, width - 1), (height - 1, 0), \
                (height - 1, width - 1):
        rows[y][x] = CORNER
    return rows

if __name__ == '__main__':
    main()
