# wysokość drzewa: h = log2(n!)
# liczba_elementów drzewa: (2**n)-1

import random
import time
import matplotlib.pyplot as plt
import numpy as np


def heapsort_HP(lista):
    """
    Własna implementacja sortowania przez kopcowanie.
    """
    n = len(lista)
    #pętla zapewniająca spełnienie założeń na każdym poziomie drzewka
    for i in range(n//2 - 1, -1, -1):
        kopce(lista, i, n-1)

    #pętla faktycznie sortująca
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        kopce(lista, 0, i-1)

    return lista


def kopce(lista, i_ref, m):
    """
    Pomocnicza funkcja do utrzymywania własności kopca.
    """
    i_left = i_ref * 2 + 1
    i_right = i_left + 1

    if i_right <= m and lista[i_left] < lista[i_right]:
        if lista[i_right] > lista[i_ref]:
            lista[i_right], lista[i_ref] = lista[i_ref], lista[i_right]
            kopce(lista, i_right, m)
        else:
            return lista

        if lista[i_left] > lista[i_ref]:
            lista[i_left], lista[i_ref] = lista[i_ref], lista[i_left]
            kopce(lista, i_left, m)
        else:
            return lista

    elif i_left <= m and lista[i_left] > lista[i_ref]:
        lista[i_left], lista[i_ref] = lista[i_ref], lista[i_left]
        kopce(lista, i_left, m)
    else:
        return lista


def heap_sort_i(x):
    """
    Iteracyjna implementacja sortowania przez kopcowanie.
    """
    first = 0
    length = len(x)
    l = first + length // 2 + 1
    r = first + length - 1
    ok = (r > 0)
    while ok:
        if l > first:
            l -= 1
            t = x[l]
        else:
            t = x[r]
            x[r] = x[first]
            r -= 1
            if r == first:
                x[first] = t
                ok = False
        i = l
        j = l + l + 1
        while j <= r:
            if j < r:
                if x[j] < x[j + 1]:
                    j += 1
            if t < x[j]:
                x[i] = x[j]
                i = j
                j = j + j + 1
            else:
                j = r + 1
        x[i] = t
    return x


def heap_sort_r(x):
    """
       Rekurencyjna implementacja sortowania przez kopcowanie.
       """
    n = len(x)
    for i in range(n // 2 - 1, -1, -1):
        heapify(x, n, i)
    for i in range(n - 1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heapify(x, i, 0)
    return x


def heapify(x, n, i):
    """
        Pomocnicza funkcja do rekurencyjnego sortowania przez kopcowanie.
        """
    m = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and x[i] < x[l]:
        m = l
    if r < n and x[m] < x[r]:
        m = r
    if m != i:
        x[i], x[m] = x[m], x[i]
        heapify(x, n, m)

def time_it(funkcja,i):
    t = time.time()
    funkcja(i)
    t_res = time.time() - t
    return t_res



# Porównanie czasów działania różnych implementacji
heap_HP = []
heap_JJ_i = []
heap_JJ_r = []

lista_list = [[random.uniform(1, 100) for _ in range(10000)] for _ in range(1, 100)]

for lista_testowa in lista_list:
    lista1 = lista_testowa[:]
    lista2 = lista_testowa[:]
    lista3 = lista_testowa[:]

    a = time_it(heapsort_HP, lista1)
    b = time_it(heap_sort_i, lista2)
    c = time_it(heap_sort_r, lista3)

    assert lista1 == lista2 == lista3, "Sortowania nie są spójne!"
    heap_HP.append(a)
    heap_JJ_i.append(b)
    heap_JJ_r.append(c)

# Analiza wyników
print(f"Średnie czasy dla:\n"
      f"HP: {np.mean(heap_HP):.6f} s,\n"
      f"JJ_i: {np.mean(heap_JJ_i):.6f} s,\n"
      f"JJ_r: {np.mean(heap_JJ_r):.6f} s.")

# Wizualizacja wyników
x = np.arange(len(heap_HP))
plt.figure(figsize=(10, 6))
plt.plot(x, heap_HP, color='red', label='Heapsort HP')
plt.plot(x, heap_JJ_i, color='blue', label='Iteracyjny Heapsort JJ')
plt.plot(x, heap_JJ_r, color='green', label='Rekurencyjny Heapsort JJ')

plt.title("Porównanie czasów działania implementacji sortowania przez kopcowanie")
plt.xlabel("Numer testu")
plt.ylabel("Czas wykonania [s]")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()