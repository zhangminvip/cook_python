import os
import sys
import tempfile


def main():
    print(len(sys.argv), sys.argv[0])
    if len(sys.argv) > 1 and sys.argv[1] == '-P':
        create_diagram(DiagramFactory()).save(sys.stdout)
        return

    textFilename = os.path.join(os.getcwd(), "diagram.txt")
    create_diagram(DiagramFactory()).save(textFilename)
    print('wrote', textFilename)


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4,1, 22, 5, 'yellow')
    text = factory.make_text(7, 3, 'Abstract Factory')
    diagram.add(rectangle)
    diagram.add(text)
    return diagram

    # F1
    # for x,l in enumerate(diagram.diagram):
    #     s = ''
    #     for y,char in enumerate(l):
    #         s += char
    #     print(s)

    # F2
    # for x in range(len(diagram.diagram)):
    #     s = ''
    #     for y in range(len(diagram.diagram[x])):
    #         s += diagram.diagram[x][y]
    #     print(s)

    return diagram



class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill='white',
                       stroke='black'):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


class SvgDiagramFactory(DiagramFactory):

    def make_diagram(self, width, height):
        return SvgDiagram(width, height)


    def make_rectangle(self, x, y, width, height, fill="white",
            stroke="black"):
        return SvgRectangle(x, y, width, height, fill, stroke)


    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)





BLANK = ' '
CORNER = '+'
HORIZONTAL = '-'
VERTICAL = '|'


class Diagram:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.diagram = _create_rectangle(self.width, self.height, BLANK)

    def add(self, component):
        for y, row in enumerate(component.rows):
            for x, char in enumerate(row):
                self.diagram[y + component.y][x + component.x] = char

    def save(self, filenameOrFile):
        file = None if isinstance(filenameOrFile, str) else filenameOrFile
        try:
            if file is None:
                file = open(filenameOrFile, "w", encoding="utf-8")
            for row in self.diagram:
                print("".join(row), file=file)
        finally:
            if isinstance(filenameOrFile, str) and file is not None:
                file.close()





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


class Rectangle:

    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.rows = _create_rectangle(width, height,
                                      BLANK if fill == 'white' else '%')

class Text:

    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]


SVG_START = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
    "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg xmlns="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve"
    width="{pxwidth}px" height="{pxheight}px">"""

SVG_END = "</svg>\n"

SVG_RECTANGLE = """<rect x="{x}" y="{y}" width="{width}" \
height="{height}" fill="{fill}" stroke="{stroke}"/>"""

SVG_TEXT = """<text x="{x}" y="{y}" text-anchor="left" \
font-family="sans-serif" font-size="{fontsize}">{text}</text>"""

SVG_SCALE = 20


if __name__ == '__main__':
    main()
