n = int(input("Add meg a gépek számát (n): "))
t = int(input("Add meg a gyártandó termékek számát (t): "))
gepek = list(map(int, input(f"Add meg a {n} számú gép {n} db gyártási idejét gyártási idejét (szóközzel elválasztva): ").split()))

bal = 0
jobb = min(gepek) * t
valasz = jobb

while bal <= jobb:
    mid = (bal + jobb) // 2
    legyartott = sum(mid // k for k in gepek)

    if legyartott >= t:
        valasz = mid
        jobb = mid - 1
    else:
        bal = mid + 1
print(f"\nA minimális idő, amennyi alatt {t} termék elkészül: {valasz} másodperc.")
