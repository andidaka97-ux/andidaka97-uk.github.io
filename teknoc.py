import turtle

turtle.setup(width=900, height=800)
rajz = turtle.Turtle()
rajz.speed(0)
rajz.hideturtle()

NAGY = 150
KOZEPES = NAGY / 3
KICSI = NAGY / 9
KEZDO_X, KEZDO_Y = -225, 225

def menj_ide(x, y):
    rajz.penup()
    rajz.goto(x, y)
    rajz.setheading(0)
    rajz.pendown()

def negyzet(x, y, oldal):
    menj_ide(x, y)
    for _ in range(4):
        rajz.forward(oldal)
        rajz.right(90)

def kis_negyzet_blokk(alap_x, alap_y, sor, oszlop):
    for r in range(3):
        for c in range(3):
            x = alap_x + (oszlop * 3 + c) * KICSI
            y = alap_y - (sor * 3 + r) * KICSI
            negyzet(x, y, KICSI)

def resz_sarok(alap_x, alap_y, sarok):
    if sarok == 'bf':
        blokkok = [(0, 0), (0, 1), (1, 0)]
    elif sarok == 'jf':
        blokkok = [(0, 1), (0, 2), (1, 2)]
    elif sarok == 'ba':
        blokkok = [(1, 0), (2, 0), (2, 1)]
    else:
        blokkok = [(1, 2), (2, 1), (2, 2)]

    for br, bc in blokkok:
        kis_negyzet_blokk(alap_x, alap_y, br, bc)

def kis_negyzetek_nagyban(alap_x, alap_y, cella_sor, cella_oszlop, kis_koord):
    bx = alap_x + cella_oszlop * KOZEPES
    by = alap_y - cella_sor * KOZEPES
    for (r, c) in kis_koord:
        x = bx + c * KICSI
        y = by - r * KICSI
        negyzet(x, y, KICSI)


def L_alak(alap_x, alap_y, cella_sor, cella_oszlop, sarok):
    if sarok == 'bf':
        koord = [(0, 0), (0, 1), (1, 0)]
    elif sarok == 'jf':
        koord = [(0, 2), (0, 1), (1, 2)]
    elif sarok == 'ba':
        koord = [(2, 0), (1, 0), (2, 1)]
    else:  # 'ja'
        koord = [(2, 2), (1, 2), (2, 1)]
    kis_negyzetek_nagyban(alap_x, alap_y, cella_sor, cella_oszlop, koord)


def nagy_fraktal(alap_x, alap_y):
    negyzet(alap_x, alap_y, NAGY)

    osszes_kis = [(r, c) for r in range(3) for c in range(3)]
    kihagy = {(1, 1)}

    def oldalso_cella(sor, oszlop):
        for (r, c) in osszes_kis:
            if (r, c) in kihagy:
                continue
            x = alap_x + oszlop * KOZEPES + c * KICSI
            y = alap_y - sor * KOZEPES - r * KICSI
            negyzet(x, y, KICSI)

    oldalso_cella(0, 1)
    oldalso_cella(1, 0)
    oldalso_cella(1, 2)
    oldalso_cella(2, 1)

    L_alak(alap_x, alap_y, 0, 0, 'bf')
    L_alak(alap_x, alap_y, 0, 2, 'jf')
    L_alak(alap_x, alap_y, 2, 0, 'ba')
    L_alak(alap_x, alap_y, 2, 2, 'ja')

    bx = alap_x + 2 * KOZEPES + KICSI
    by = alap_y - 3 * KOZEPES - 2 * KICSI + 3 * KICSI
    negyzet(bx, by, KICSI)


def giga_kontur():
    teljes = NAGY * 3
    alap_x, alap_y = KEZDO_X, KEZDO_Y
    negyzet(alap_x, alap_y, teljes)

    for i in range(1, 3):
        menj_ide(alap_x + i * NAGY, alap_y)
        rajz.right(90)
        rajz.forward(teljes)
        rajz.left(90)

    for i in range(1, 3):
        menj_ide(alap_x, alap_y - i * NAGY)
        rajz.forward(teljes)


def giga_fraktal():
    for r in range(3):
        for c in range(3):
            alap_x = KEZDO_X + c * NAGY
            alap_y = KEZDO_Y - r * NAGY

            if (r, c) == (1, 1):
                continue

            if (r, c) == (0, 0):
                resz_sarok(alap_x, alap_y, 'bf')
                continue
            if (r, c) == (0, 2):
                resz_sarok(alap_x, alap_y, 'jf')
                continue
            if (r, c) == (2, 0):
                resz_sarok(alap_x, alap_y, 'ba')
                continue
            if (r, c) == (2, 2):
                resz_sarok(alap_x, alap_y, 'ja')
                continue

            nagy_fraktal(alap_x, alap_y)

    giga_kontur()

giga_fraktal()
turtle.done()
