def ggT(a, b):
    """
    Berechnung des ggT mit hilfe des Euklidischen Algorithmus

    :param a: zahl 1 > b
    :param b: zahl 2
    :return: gröster gemeinsamer Teiler
    """

    while b != 0:
        a, b = b, a % b
        return a


def extend_ggT(a, b):
    if a == 0:
        return b, 0, 1
    else:
        ggT, x, y = extend_ggT(b % a, a)
        return ggT, y - (b // a) * x, x

def chinesicher_Restsatz(n, a):
    """

    :param n: liste von teilerfremden Moduli
    :param a: liste von Resten, die bezüglich der Modili n erfüllen müssen
    :return:
    """
    N = 1
    for i in range(len(n)):
        # erstellen des KGV (kleinstes geminsames Vielfaches)
        N *= n[i]

    X = 0
    for i in range(len(n)):
        m = N // n[i]
        ggT, inverse, _ = extend_ggT(m, n[i])
        X += a[i] * inverse * m

    return X % N


def start():
    while True:
        n = input("Bitte geben Sie die Moduli durch Leerzeichen getrennt ein: ")
        a = input("Bitte geben Sie die Reste durch Leerzeichen getrennt ein: ")
        n = list(map(int, n.split()))
        a = list(map(int, a.split()))
        x = chinesicher_Restsatz(n, a)
        print("Die Lösung ist x =", x)


if __name__ == '__main__':
    start()
