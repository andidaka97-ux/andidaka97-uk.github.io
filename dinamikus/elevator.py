n = int(input("Add meg az emberek számát (n): "))
x = int(input("Add meg a lift maximális teherbírását (x): "))
w = list(map(int, input(f"Add meg a {n} ember súlyát szóközzel elválasztva: ").split()))

dp = [(n + 1, 0)] * (1 << n)
dp[0] = (1, 0)
for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            prev = mask ^ (1 << i)
            rides, weight = dp[prev]

            if weight + w[i] <= x:
                new = (rides, weight + w[i])
            else:
                new = (rides + 1, w[i])

            if new < dp[mask]:
                dp[mask] = new

print(f"\nA minimális liftmenetek száma: {dp[(1 << n) - 1][0]}")
