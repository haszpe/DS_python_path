def fun(x):
    """
    Funkcja testowa: f(x) = 2x + 4.
    """
    return 2 * x + 4


def osacz(x, funkcja):
    """
    Metoda iteracji prostej - osaczenie miejsca zerowego.
    Znajduje przedział, w którym funkcja zmienia znak.
    """
    k = 1
    y = funkcja(x)
    xp, xpp = x, x  # xp - ostatni krok, xpp - przedostatni krok

    while funkcja(x) * y > 0:
        xpp, xp = xp, x
        x += k
        k = -1.1 * k
        y = funkcja(x)

    if funkcja(x) == 0:
        return x
    return xp, xpp



def osacz_lista(x, funkcja):
    """
    Metoda iteracji prostej z przechowywaniem kroków w liście.
    Znajduje przedział, w którym funkcja zmienia znak.
    """
    k = 1
    y = funkcja(x)
    lista_x = [x, x, x]
    yp = y
    while (y * yp) > 0:
        x = x + k
        lista_x.append(x)
        lista_x.pop(0)
        k = -1.1*k
        yp = y
        y = fun(x)
    if y == 0:
        return x
    lista_x.pop(1)
    return lista_x

def osacz_debug(x, funkcja):
    """
    Wersja debugująca metody iteracji prostej - drukuje kroki osaczenia.
    """
    k = 1
    y = funkcja(x)
    lista_x = [x, x, x]
    yp = y
    while (y * yp) > 0:
        print(y, yp, lista_x)
        x = x + k
        lista_x.append(x)
        k = -1.1 * k
        yp = y
        y = fun(x)
    if y == 0:
        return x
    return lista_x[-3], lista_x[-1]


def bisekcja(funkcja, a, b, eps):
    """
    Metoda bisekcji - znajdowanie miejsca zerowego funkcji przez podział przedziału na pół.

    Args:
        funkcja (callable): Funkcja, dla której szukamy miejsca zerowego.
        a (float): Lewa granica przedziału.
        b (float): Prawa granica przedziału.
        eps (float): Tolerancja wyniku.
    """
    ya = funkcja(a)
    yb = funkcja(b)
    while (ya * yb) < 0:
        s = (a + b) / 2
        ys = funkcja(s)
        if (ya * ys) < 0:
            b = s
            yb = funkcja(b)
        elif (yb * ys) < 0:
            a = s
            ya = funkcja(a)
        else:
            return s

        if (abs(a - b)) < eps:
            return (a + b) / 2
    raise ValueError('Niespełniony warunek - miejsce zerowe nie znajduje się w zadanym przedziale')


def met_stycznych(f, x0, pochodna, eps):
    """
    Metoda stycznych - znajdowanie miejsca zerowego funkcji za pomocą iteracji Newtona.
    """
    x = x0
    y = f(x)
    while abs(y) >= eps:
        yprim = pochodna(x)
        x -= y / yprim
        y = f(x)
    return x


if __name__ == "__main__":

    print(f"Metoda osaczania | znalezione miejsce zerowe w przedziale {osacz(2, fun)}")
    print(f"Metoda osaczania | znalezione miejsce zerowe w przedziale {osacz_lista(2, fun)}")
    print(osacz_debug(2, fun))

    # Bisekcja - funkcja kwadratowa
    def f(x):
        return -x ** 2 + 4
    try:
        print(bisekcja(f, -100, 100, 0.001))
    except ValueError as e:
        print(e)

    # Metoda stycznych
    def pochodna(x):
        return -2 * x
    print(f"Metoda stycznych | znalezione miejsce zerowe w {met_stycznych(f, 1.0, pochodna, 0.001)}")
