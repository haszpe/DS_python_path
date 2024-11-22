'''
Wybrane operacje na grafie reprezentowanym jako lista sąsiedztwa:
    Podstawowe operacje:
        Odczyt grafu z pliku.
        Sprawdzanie symetrii połączeń.
        Symetryzacja połączeń.

Algorytmy dla grafów nieskierowanych (o symetrycznych krawędziach):
    Przeszukiwanie wszerz (BFS) – iteracyjne, z użyciem kolejki.
    Wyznaczanie składowych spójnych za pomocą BFS.
    Przeszukiwanie w głąb (DFS) – rekurencyjne.
    Przeszukiwanie w głąb (DFS) – iteracyjne, z użyciem stosu.
'''


def czytaj_liste_sasiedztw(sciezka):
    """
    Wczytuje graf w formacie listy sąsiedztw z pliku.
    Format pliku:
    - Pierwszy wiersz jest pomijany
    - Każdy kolejny wiersz: wierzchołek oraz jego sąsiedzi, rozdzieleni spacjami
    - Puste wiersze są ignorowane
    """
    graf = {}
    with open(sciezka) as plik:
        plik.readline()  # Pomijanie pierwszego wiersza
        for wiersz in plik:
            dane = wiersz.split()
            if dane:
                wierzcholek = dane.pop(0)
                if wierzcholek in graf:
                    raise ValueError(f"Wierzchołek {wierzcholek} został zdefiniowany więcej niż raz.")
                graf[wierzcholek] = dane

    # Walidacja poprawności grafu
    for x in graf:
        for y in graf[x]:
            if y not in graf:
                raise ValueError(f"Nieznany wierzchołek {y} występuje jako sąsiad {x}.")
    return graf


def czy_symetryczny(graf):
    """
    Sprawdza, czy graf jest symetryczny (każda krawędź ma przeciwbieżny odpowiednik).
    Zwraca listę niesymetrycznych krawędzi.
    """
    niesymetryczne = []
    for x in graf:
        for y in graf[x]:
            if x not in graf[y]:
                niesymetryczne.append((x,y))
    return niesymetryczne


def uzupelnij_przeciwbiezne(graf, krawedzie):
    """
    Dodaje brakujące krawędzie przeciwbieżne do grafu.
    """
    for x, y in krawedzie:
        if x not in graf or y not in graf:
            raise ValueError(f"Krawędź odnosi się do nieistniejącego wierzchołka: {x} -> {y}")
        graf[y].append(x)


def bfs(graf, start, visited=None, oznacz=1):
    """
    Przeszukiwanie wszerz (Breadth-First Search).
    Zwraca listę wierzchołków należących do komponentu spójności zawierającego `start`.
    """
    assert start in graf
    assert bool(oznacz)

    if visited is None:
        visited = {x: None for x in graf}

    queue = [start]
    spin_graf = {}
    while queue:
        v = queue.pop(0)
        if not visited[v]:
            print('BFS: wchodzę do {}'.format(v))
            visited[v] = oznacz

            for vn in graf[v]:
                queue.append(vn)
                not_yet_visited = graf[vn]
                for i in not_yet_visited:
                    if visited[i]:
                        x = 0
                spin_graf[v] = not_yet_visited

    return [x for x in visited if visited[x] == oznacz ]


def rozbicie(graf):
    """
    Wyznacza składowe spójne grafu, zwracając listę list wierzchołków należących do poszczególnych składowych.
    """
    result = []
    visited = {x: None for x in graf}
    i = 0
    for x in graf:
        if not visited[x]:
            i += 1
            r = bfs(graf, x, visited, i)
            result.append(r)
    return result


def dfs_rekurencyjny(graf, start, visited=None, oznacz=1):
    """
        Rekurencyjne przeszukiwanie w głąb (Depth-First Search).
        """
    assert bool(oznacz)
    assert start in graf
    if visited is None:
        visited = {x: None for x in graf}

    if not visited[start]:
        print(f"DFS Rek: wchodzę do  {start}")
        visited[start] = oznacz
        for sasiad in graf[start]:
            dfs_rekurencyjny(graf, sasiad, visited, oznacz)
        print(f'DFS rekurencyjny: wychodzę z {start}')
    return [x for x in visited if visited[x] == oznacz]


def dfs_iteracyjny(graf, start, visited=None, oznacz=1):
    """
    Iteracyjne przeszukiwanie w głąb (Depth-First Search) z wykorzystaniem stosu.
    """
    assert start in graf
    assert bool(oznacz)
    if visited is None:
        visited = {x: None for x in graf}

    queue = [start]
    while queue:
        v = queue.pop(-1)
        if not visited[v]:
            # previsit vn
            print(f'DFS iteracyjny: wchodzę do {v}')
            visited[v] = oznacz
            for vn in graf[v]:
                queue.append(vn)
    return [x for x in visited if visited[x] == oznacz]


if __name__ == '__main__':
    import sys

    # Pobieranie argumentów wejściowych
    #sciezka = sys.argv[1]
    #wierzcholek = sys.argv[2]
    sciezka = 'lista.txt'
    wierzcholek = 'A'

    # Wczytanie grafu
    graf = czytaj_liste_sasiedztw(sciezka)
    print("Graf wczytany:", graf)
    assert wierzcholek in graf

    # Sprawdzenie symetrii
    niesymetryczne = czy_symetryczny(graf)
    print("Czy graf jest symetryczny:", not niesymetryczne)

    # BFS
    print("Przeszukiwanie wszerz:")
    print(bfs(graf, wierzcholek))

    # DFS (rekurencyjny)
    print("Przeszukiwanie w głąb (rekurencyjnie):")
    print(dfs_rekurencyjny(graf, wierzcholek))

    # DFS (iteracyjny)
    print("Przeszukiwanie w głąb (iteracyjnie):")
    print(dfs_iteracyjny(graf, wierzcholek))

    # Wyznaczanie składowych spójnych
    print("Składowe spójne grafu:")
    print(rozbicie(graf))
