import svgwrite
import random


def add_node(path, x1, y1, x2, y2, xx, yy):
    path.push('C%f,%f %f,%f %f,%f' % (
        x1, y1,
        x2, y2,
        xx, yy
    ))

def main():
    width = 800
    height = 600
    cut_w, cut_h = 50, 50

    offset_array = [-2, -1, 0, 1, 2]

    dwg = svgwrite.Drawing('jigsaw_puzzle.svg', height=height, width=width)
    dwg.add(dwg.rect((0, 0), (width, height), stroke='black', fill='none'))
    prevx = 0
    for x in range(cut_w, width, cut_w):
        rows = svgwrite.path.Path(stroke='red', fill='none')
        rows.push('M %f,%f' % (x, 0))
        prevy = 0
        for y in range(cut_h, height + cut_h, cut_h):
            offset = random.choice(
                [
                    -cut_w / 4, cut_w / 4,
                    -cut_w / 3, cut_w / 3,
                ])
            delta = x - cut_w / 4 if offset > 0 else x + cut_w / 4
            xval = x + offset

            x1 = delta
            y1 = y - 5
            x2 = xval
            y2 = prevy
            xx = xval
            yy = y - cut_h / 2
            add_node(rows, x1, y1, x2, y2, xx, yy)

            x1 = xval
            y1 = y
            x2 = delta
            y2 = prevy + 5
            xx = x
            yy = y
            add_node(rows, x1, y1, x2, y2, xx, yy)

            prevy = y

        dwg.add(rows)
        prevx = x

    for y in range(cut_h, height, cut_h):
        cols = svgwrite.path.Path(stroke='blue', fill='none')
        cols.push('M %f,%f' % (0, y))
        prevx = 0
        for x in range(cut_w, width + cut_w, cut_w):
            offset = random.choice([
                -cut_h / 4, cut_h / 4,
                -cut_h / 3, cut_h / 3
            ])
            delta = y - cut_h/4 if offset > 0 else y + cut_h / 4
            yval = y + offset

            x1 = x - 5
            y1 = delta
            x2 = prevx
            y2 = yval
            xx = x - cut_w / 2
            yy = yval
            add_node(cols, x1, y1, x2, y2, xx, yy)

            x1 = x
            y1 = yval
            x2 = prevx + 5
            y2 = delta
            xx = x
            yy = y
            add_node(cols, x1, y1, x2, y2, xx, yy)

            prevx = x

        dwg.add(cols)
    dwg.save()


if __name__ == '__main__':
    main()