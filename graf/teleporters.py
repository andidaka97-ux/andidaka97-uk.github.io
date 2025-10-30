import sys
sys.setrecursionlimit(300000)

n, m = map(int, input("Add meg a szintek és teleportok számát (pl. 5 6): ").split())

szomszed = [[] for _ in range(n + 1)]
be = [0] * (n + 1)
ki = [0] * (n + 1)

print("Add meg a teleportokat (pl. 1 2):")
for _ in range(m):
    a, b = map(int, input().split())
    szomszed[a].append(b)
    ki[a] += 1
    be[b] += 1

if ki[1] - be[1] != 1 or be[n] - ki[n] != 1:
    print("IMPOSSIBLE")
    sys.exit()

for i in range(2, n):
    if be[i] != ki[i]:
        print("IMPOSSIBLE")
        sys.exit()

útvonal = []
mutato = [0] * (n + 1)

def bejár(v):
    while mutato[v] < len(szomszed[v]):
        u = szomszed[v][mutato[v]]
        mutato[v] += 1
        bejár(u)
    útvonal.append(v)

bejár(1)
útvonal.reverse()

if len(útvonal) != m + 1 or útvonal[-1] != n:
    print("IMPOSSIBLE")
else:
    print(" ".join(map(str, útvonal)))
