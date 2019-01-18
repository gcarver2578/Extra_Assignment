# Gabriel Carver
import random
import graphics as g


def main():
    dice()


def dice():
    d_win = g.GraphWin("Dice", 325, 450)
    d_win.setBackground('White')
    _close_ = g.Rectangle(g.Point(275, 0), g.Point(325, 50))
    close_text = g.Text(g.Point(300, 25), 'Done')
    _close_.setFill('red')
    close_text.setStyle('bold')
    close_text.setFill('white')
    draw_stuff = [_close_, close_text]
    for item in draw_stuff:
        item.draw(d_win)
    rolls = [0, 0, 0, 0, 0]
    for i in range(5):
        rolls[i] = random.randint(1, 6)
    draw_dice(rolls, d_win)
    d_win.getMouse()
    clear(d_win)
    d_win.getMouse()


def draw_dice(rolls, d_win):
    print(rolls)
    starting_points_y = [25, 125, 225]
    colors = ["Red", "Green", "Blue", "Black", "Orange", "Gold", "Cyan", "Pink", "Purple"]
    r_index = 0
    # prints out dice without numbers
    for s_x in starting_points_y[:2]:
        for s_y in starting_points_y:
            points = [g.Point(0 + s_x, 0 + s_y), g.Point(0 + s_x, 75 + s_y), g.Point(75 + s_x, 75 + s_y),
                      g.Point(75 + s_x, 0 + s_y)]
            square = g.Polygon(points)
            square.draw(d_win)
            square.setFill(colors[random.randint(0, len(colors) - 1)])
            # cases for which dots to draw
            if rolls[r_index] == 1:
                continue
            elif rolls[r_index] == 2:
                continue
            elif rolls[r_index] == 3:
                continue
            elif rolls[r_index] == 4:
                continue
            elif rolls[r_index] == 5:
                continue
            else:
                continue
    # points for each side of the dice
    s_1 = [g.Point(25 + 37.5, 25 + 37.5)]
    s_2 = [g.Point(25 + 12.5, 125 + 12.5), g.Point(25 + 62.5, 125 + 62.5)]
    s_3 = [g.Point(25 + 12.5, 225 + 62.5), g.Point(25 + 37.5, 225 + 37.5), g.Point(25 + 62.5, 225 + 12.5)]
    s_4 = [g.Point(125 + 12.5, 25 + 12.5), g.Point(125 + 12.5, 25 + 62.5), g.Point(125 + 62.5, 25 + 12.5),
           g.Point(125 + 62.5, 25 + 62.5)]
    s_5 = [g.Point(125 + 12.5, 125 + 12.5), g.Point(125 + 12.5, 125 + 62.5), g.Point(125 + 62.5, 125 + 12.5),
           g.Point(125 + 62.5, 125 + 62.5), g.Point(125 + 37.5, 125 + 37.5)]
    s_6 = [g.Point(125 + 12.5, 225 + 12.5), g.Point(125 + 12.5, 225 + 62.5), g.Point(125 + 62.5, 225 + 12.5),
           g.Point(125 + 62.5, 225 + 62.5), g.Point(125 + 12.5, 225 + 37.5), g.Point(125 + 62.5, 225 + 37.5)]
    sides = [s_1, s_2, s_3, s_4, s_5, s_6]
    # prints out dots on dice
    for side in sides:
        for center in side:
            c = g.Circle(center, 7)
            c.draw(d_win)
            c.setFill("White")


# clears the screen
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


# returns if any of the given points is inside a given box
def inside(points, tl, br):
    for point in points:
        x = point.getX()
        y = point.getY()
        if (br.getX() > x > tl.getX()) and (br.getY() > y > tl.getY()):
            return True
    return False


main()
