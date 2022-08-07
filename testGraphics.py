# https://www.youtube.com/watch?v=R39vTAj1u_8&list=PLmzkEJ1Zz_uZ5nvTOLaGHfinCzEVEVBlz
# https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

# from graphics import *
import graphics as g


def main():
    # PART 1
    win = g.GraphWin("My Window: Part 1", 500, 500)
    win.setBackground("black")  # color_rgb(255, 0, 0)

    pt = g.Point(250, 250)
    cir = g.Circle(pt, 50)  # Circle(Point(250, 250), 50)
    cir.setFill(g.color_rgb(100, 255, 50))
    cir.draw(win)

    win.getMouse()
    win.close()

    # -----------------------------------------------------------

    # PART 2
    win = g.GraphWin("My Window: Part 2", 500, 500)
    win.setBackground("black")  # color_rgb(255, 0, 0)

    pt1 = g.Point(250, 250)
    # pt1.setOutline(g.color_rgb(255, 255, 0))
    # pt1.draw(win)
    pt2 = g.Point(250, 350)
    ln = g.Line(pt1, pt2)
    ln.setFill(g.color_rgb(0, 255, 255))
    ln.setWidth(10)
    ln.draw(win)

    rect = g.Rectangle(g.Point(100, 50), g.Point(300, 150))
    rect.setOutline("yellow")
    rect.setFill("magenta")
    rect.setWidth(5)
    rect.draw(win)

    win.getMouse()
    win.close()

    # -----------------------------------------------------------

    # PART 3


main()
