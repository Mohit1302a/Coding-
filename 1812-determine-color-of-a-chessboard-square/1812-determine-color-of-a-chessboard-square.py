class Solution(object):
    def squareIsWhite(self, coordinates):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8

        column = coordinates[0]
        row = int(coordinates[1])

        if column == 'a':
            value = a
        elif column == 'b':
            value = b
        elif column == 'c':
            value = c
        elif column == 'd':
            value = d
        elif column == 'e':
            value = e
        elif column == 'f':
            value = f
        elif column == 'g':
            value = g
        else:
            value = h

        # White when column number and row number have different parity
        if (value + row) % 2 == 1:
            return True
        return False