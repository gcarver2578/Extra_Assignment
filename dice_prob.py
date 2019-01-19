# Gabriel Carver
import random
import graphics as g
# import time
# important stuff that needs to be accessed in different functions
_close_ = g.Rectangle(g.Point(275, 0), g.Point(325, 50))
close_text = g.Text(g.Point(300, 25), 'Done')
_close_.setFill('black')
_roll_ = g.Rectangle(g.Point(275, 50), g.Point(325, 100))
roll_text = g.Text(g.Point(300, 75), 'Roll')
_roll_.setFill(g.color_rgb(98, 166, 255))
_sim_ = g.Rectangle(g.Point(275, 100), g.Point(325, 150))
sim_text = g.Text(g.Point(300, 125), 'Sim')
_sim_.setFill('blue')
_res_ = g.Rectangle(g.Point(275, 150), g.Point(325, 200))
res_text = g.Text(g.Point(300, 175), 'Reset')
_res_.setFill('red')
inp = g.Entry(g.Point(-20, 0), 10)
num_rolls = -1
perfect_rolls = -1
n_text = g.Text(g.Point(100, 420), 'Rolls: 0')
p_text = g.Text(g.Point(100, 435), 'Five of a Kinds: 0')
per_text = g.Text(g.Point(250, 435), '0%')
draw_stuff = [_close_, close_text, _sim_, sim_text, _roll_, roll_text, inp, n_text, p_text, per_text, _res_, res_text]
for _item_ in [close_text, roll_text, sim_text, res_text]:
    _item_.setStyle('bold')
    _item_.setFill('white')


def main():
    dice()


def dice():
    global num_rolls, perfect_rolls
    d_win = g.GraphWin("Dice", 325, 450)
    d_win.setBackground('White')
    rolls = [1] * 5
    draw_dice(rolls, d_win)
    update_stats(rolls)
    m = d_win.getMouse()
    while True:
        while not inside([m], _close_.getP1(), _res_.getP2()):
            m = d_win.getMouse()
        # ends the program
        if inside([m], _close_.getP1(), _close_.getP2()):
            d_win.close()
            return
        # does one roll
        elif inside([m], _roll_.getP1(), _roll_.getP2()):
            clear(d_win)
            rolls = reroll(rolls)
            draw_dice(rolls, d_win)
            update_stats(rolls)
            m = d_win.getMouse()
        # simulates rolls until a 5 of a kind
        elif inside([m], _sim_.getP1(), _sim_.getP2()):
            inp.setText('')
            rolls = reroll(rolls)
            while rolls.count(rolls[0]) != 5 and ' ' not in inp.getText():
                clear(d_win)
                rolls = reroll(rolls)
                draw_dice(rolls, d_win)
                update_stats(rolls)
            m = d_win.getMouse()
        else:
            num_rolls = -1
            perfect_rolls = -1
            rolls = [1] * 5
            clear(d_win)
            update_stats(rolls)
            draw_dice(rolls, d_win)
            m = d_win.getMouse()


def draw_dice(rolls, d_win):
    for item in draw_stuff:
        item.draw(d_win)
    starting_points_y = [25, 125, 225]
    colors = ["Red", "Green", "Blue", "Black", "Orange", "Gold", "Cyan", "Pink", "Purple"]
    r_index = 0
    # prints out dice without dots
    for s_x in starting_points_y[:2]:
        for s_y in starting_points_y:
            if r_index == 5:
                break
            points = [g.Point(0 + s_x, 0 + s_y), g.Point(0 + s_x, 75 + s_y), g.Point(75 + s_x, 75 + s_y),
                      g.Point(75 + s_x, 0 + s_y)]
            square = g.Polygon(points)
            square.draw(d_win)
            square.setFill(colors[random.randint(0, len(colors) - 1)])
            # cases for which dots to draw
            if rolls[r_index] == 1:
                dots = [g.Point(s_x + 37.5, s_y + 37.5)]
            elif rolls[r_index] == 2:
                dots = [g.Point(s_x + 12.5, s_y + 12.5), g.Point(s_x + 62.5, s_y + 62.5)]
            elif rolls[r_index] == 3:
                dots = [g.Point(s_x + 12.5, s_y + 62.5), g.Point(s_x + 37.5, s_y + 37.5),
                        g.Point(s_x + 62.5, s_y + 12.5)]
            elif rolls[r_index] == 4:
                dots = [g.Point(s_x + 12.5, s_y + 12.5), g.Point(s_x + 12.5, s_y + 62.5),
                        g.Point(s_x + 62.5, s_y + 12.5), g.Point(s_x + 62.5, s_y + 62.5)]
            elif rolls[r_index] == 5:
                dots = [g.Point(s_x + 12.5, s_y + 12.5), g.Point(s_x + 12.5, s_y + 62.5),
                        g.Point(s_x + 62.5, s_y + 12.5), g.Point(s_x + 62.5, s_y + 62.5),
                        g.Point(s_x + 37.5, s_y + 37.5)]
            elif rolls[r_index] == 6:
                dots = [g.Point(s_x + 12.5, s_y + 12.5), g.Point(s_x + 12.5, s_y + 62.5),
                        g.Point(s_x + 62.5, s_y + 12.5), g.Point(s_x + 62.5, s_y + 62.5),
                        g.Point(s_x + 12.5, s_y + 37.5), g.Point(s_x + 62.5, s_y + 37.5)]
            else:
                dots = []
            for dot in dots:
                c = g.Circle(dot, 7)
                c.draw(d_win)
                c.setFill('white')
            r_index += 1


# rerolls the dice
def reroll(rolls):
    for i in range(len(rolls)):
        rolls[i] = random.randint(1, 6)
    return rolls


# clears the screen
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()


def update_stats(rolls):
    global num_rolls, perfect_rolls
    num_rolls += 1
    str1 = 'Rolls: ' + str(num_rolls)
    n_text.setText(str1)
    if rolls.count(rolls[0]) == 5:
        perfect_rolls += 1
    str2 = 'Five of a Kinds: ' + str(perfect_rolls)
    p_text.setText(str2)
    str3 = ''
    try:
        str3 = str(round((perfect_rolls / num_rolls) * 100, 4)) + '%'
    except ZeroDivisionError:
        str3 = '0.0%'
    finally:
        per_text.setText(str3)


# returns if any of the given points is inside a given box
def inside(points, tl, br):
    for point in points:
        x = point.getX()
        y = point.getY()
        if (br.getX() > x > tl.getX()) and (br.getY() > y > tl.getY()):
            return True
    return False


main()
