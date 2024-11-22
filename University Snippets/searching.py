#Na ważniaku: Wróblewski - Algorytmy, struktury danych i techniki programowania

import random

random.seed(7)
lista4 = [random.random() for i in range(10000)]

lista1 = ["Ania", "Max", "Krzysiu", "Piotr", "Julia", "Zofia", "Krystian"]
lista2 = [11, 43, 29, 40, 68, 30, 23]

"""
Wyszukiwanie liniowe
    stajemy na początku listy i przeszukujęmy po koleii listy
"""

# def search_lin(h, l1):
#     i = 0
#     n = len(l1)
#     while i < n:
#         if l1[i] == h:
#             return i
#         i+=1
#     return None
#
# x = search_lin("Julia", lista1)
# print(x)


"""
Wyszukiwanie linowe z modyfikacją Knuchta
    dodanie elementu na końcu listy, zawsze znajdujemy element, poza pętlą - i ==n : brak + usuń ostatni element z listy
"""

# def search_knuth(h, l1):
#     i = 0
#     l1.append(h)
#     n = len(l1)
#     while i < n and l1[i] != h:
#         i+=1
#     if i == n:
#         i = None
#     l1.pop(n-1)
#     return i
#
# y = search_knuth(0.09071301334386506, lista4)
# print(y, t)

"""
Wyszukiwanie binarne
    porządkujemy listę, sprawdzamy w połowie, odrzucamy kolejne połowy
    
    - ze sprawdzeniem trójpozycyjnym - ogranicza zakresy z dwóch stron
    
    - ze sprawdzeniem dwupozycyjnym: nie dajemy drugiego warunku ! po jednej stronie zawężamy, 
    po drugiej przyjmujemy mid. tutaj znjadujemy pierwszą szukaną wartość
    
"""

def bin_one(h, l1):
    l1.sort()
    fs = 0
    ls = len(l1)-1
    while ls-fs > 1:    # fs < ls:
        mid = (fs + ls) // 2
        print(fs, mid, ls, h, l1)
        if l1[mid] < h:
            fs = mid + 1
        elif l1[mid] > h:
            ls = mid - 1
        else:
            return mid

    #check if the last seasrch is our word, if not there is no our word return None
    if l1[fs] == h:
        return fs
    return None

    #for returning place where it should be   (not working for first and last element !!! )
    # if fs == 0:
    # elif fs == len(l1)-1
    # else ??

    # return mid
    # dobra bisekcja dale wynik następny lub równy poszukiwanemu
    #


x = bin_one("Beata", lista1)
print(x)

# sprawko
#porównaj logiczne i nielogiczne kolejności warunków - czy wpływają na wynik?
#

def bin_two(l1, h):
    l1.sort()
    fs = 0
    ls = len(l1) - 1
    while fs < ls:
        mid = (fs + ls) // 2
        print(fs, mid, ls, h, l1)
        if l1[mid] < h:
            fs = mid + 1
        else:
            ls = mid
    return fs   #tam gdzie powinien być gdyby był ale nie sprawdza stricte czy jest

"""
Wyszukiwanie z uźyciem kodów mieszanych
    tworzymy przedziały, wartości elementów listy przypisujemy poprzez obliczenia algebraiczne
    
    I. czytanie danych, tyle pustych elementów ile elementów, element idzie do kontenera o wartości obliczonej 
    z wartości elementów ( reszta z dzielenia pi przez 1, częśc ułamkową, numer * pi i reszta z dzielenia ->
    reszty z liczby niewymiernej rozmieszczają się równomiernie w przedziale
       -> funkcja wczytaj/zapisz/zakonteneruj
       
    II. klucz obliczony z poszukiwanej wartości
        -> funkcja mieszająca
        
    III. przeszukiwanie liniowe kontenera o numerze porządkowym obliczonym z klucza 
        -> lin_search
    
Idea kodowania mieszającego:
własność ekwipartycji = równego przedziału
    coś z wielokrotnością części całkowitej z liczby niewymiernej
        k - numer wyrazu ciągu 
        n - ustalona
        k*n mod 1 * n   -> int z tego daje ci pozycję jakąś może ? 
        
    przy czym musi być niewymierna ( sqrt2 / pi / e / i   => złota liczba(Fib czy coś) = (1 + sqrt5)/2 )
        
robimy de facto zdyskretyzowany obraz przedziałów 

To metoda mająca stały czas poszukiwania, ponieważ niezależnie od wartości poszukiwanej jak i wielkości przeszukiwanego
zbioru zawsze powtarzają się tylko dwa obliczenia, niewielkie różnice mogą wynikać jedynie z tej liniowej części.
"""
def key(x):
    return ln(x)

def prep(file):
    #ile jest elementów
    #   stwórz tyle pustch list
    n - liczba wierszy
    kontenery = [ [] for kontener in range(n)]
    for x in d:
        i = key(x)
        dd.append(na miejscu i, wartość x)

    # lub po mojemu:
    for f in readline(file):

        kontenery[key(f)].append(f)


    return kontenery
def search_mix():
    return



'''
Przeszukiwanie drzewa odpowiedzi/ wyszukiwania ( reTRIEval tree = TRIE TREE)
    ??? vs. 
Przeszukiwanie przyrostowe
Założenia:
        mamy sobie spis słów 
         
                          b                                            p
                             
             r            l             o                       s             t         

             a            a             $                   u  |  a         a  |  e
            
          t  |  k          $                                          (...)
          e  |  $
          $
              
Strukturą tych słów tworzymy drzewo odpowiedzi, natrafiając na znak $
 odkrywamy koniec słowa = poczukiwane słowo istnieje



'''
