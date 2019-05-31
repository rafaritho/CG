from graphics import *

win = GraphWin('face', 900, 900)
win.setCoords(-900, -900, 900, 900)
win.setBackground('black')

pt = Point(0, 0)
pt.setOutline('green')
pt.draw(win)

def aviao(x,y):
    aviao = PhotoImage(file="aviao.png")
    label = Label (root, image=aviao)
    label.pack()

def ponto(x, y):
    pt = Point(x, y)
    pt.setOutline('green')
    pt.draw(win)

def pontoAviao(x, y):
        pt = Point(x, y)
        pt.setOutline('red')
        pt.draw(win)


def pontoAeroporto(x, y):
    pt = Point(x, y)
    pt.setOutline('blue')
    pt.draw(win)

def circulo(x, y):
    ponto(x, y)
    ponto(y, x)
    ponto(y, -x)
    ponto(-x, y)
    ponto(-x, -y)
    ponto(-y, -x)
    ponto(-y, x)
    ponto(x, -y)


def reta(x, y):
    ponto(x, y)


def circParam(x, y):
    p = 1 - y

    ponto(x, y)

    while (x < y):
        x = x + 1
        if p < 0:
            p = p + (2 * x) + 1
        else:
            y = y - 1
            p = p + (2 * x) + 1 - 2 * y
        circulo(x, y)


def retaParam(x, y, xf, yf):

    p = 0
    deltx = xf - x
    delty = yf - y
    xInc = 1
    yInc = 1


    if deltx < 0:
        xInc = -1
        deltx = -deltx
    if delty < 0:
        yInc = -1
        delty = -delty
    if delty <= deltx:
        p = deltx / 2
        while (x != xf):
            ponto(x, y)
            p = p - delty
            if p < 0:
                y = y + yInc
                p = p + deltx
            x = x + xInc
    else:
        p = delty / 2
        while (y != yf):
            ponto(x, y)
            p = p - deltx
            if p < 0:
                x = x + xInc
                p = p + delty
            y = y + yInc

        ponto(x, y)

def aviao(x, y, xf, yf):

    p = 0
    deltx = xf - x
    delty = yf - y
    xInc = 1
    yInc = 1

    if deltx < 0:
        xInc = -1
        deltx = -deltx
    if delty < 0:
        yInc = -1
        delty = -delty
    if delty <= deltx:
        p = deltx / 2
        while (x != xf):
            pontoAviao(x, y)
            p = p - delty
            if p < 0:
                y = y + yInc
                p = p + deltx
            x = x + xInc
    else:
        p = delty / 2
        while (y != yf):
            pontoAviao(x, y)
            p = p - deltx
            if p < 0:
                x = x + xInc
                p = p + delty
            y = y + yInc

        pontoAviao(x, y)

def aeroporto(x, y, xf, yf):

    p = 0
    deltx = xf - x
    delty = yf - y
    xInc = 1
    yInc = 1


    if deltx < 0:
        xInc = -1
        deltx = -deltx
    if delty < 0:
        yInc = -1
        delty = -delty
    if delty <= deltx:
        p = deltx / 2
        while (x != xf):
            pontoAeroporto(x, y)
            p = p - delty
            if p < 0:
                y = y + yInc
                p = p + deltx
            x = x + xInc
    else:
        p = delty / 2
        while (y != yf):
            pontoAeroporto(x, y)
            p = p - deltx
            if p < 0:
                x = x + xInc
                p = p + delty
            y = y + yInc

        pontoAeroporto(x, y)


circParam(0, 100)
circParam(0, 300)
circParam(0, 500)
circParam(0, 700)
retaParam(800, 0, -800, 0)
retaParam(0,  -800, 0, 800)
retaParam(-580, -580, 580, 580)
retaParam(580, -580, -580, 580)

aeroporto(400, -400, 250, -250)


aviao(20, 0, 50, 0)
aviao(40, 0, 20, -20)
aviao(40, 0, 20, 20)
aviao(10, 0, 10, 5)
aviao(10, 0, 10, -5)





win.mainloop()
