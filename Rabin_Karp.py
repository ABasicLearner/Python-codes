#Some logical error has happened!!


def RabinKarp(T, P, d, q):
    n = len(P)
    m = len(P)
    h = (d ** (m-1)) % q
    t = 0
    p = 0
    for i in range(0, m):
        t = (d*t + T[i]) % q
        p = (d*p + P[i]) % q
    for s in range(0, n-m+1):
        if t == p:
            if T[s+1:s+m] == P[1:m]:
                print(f"Matching string found after {s} shifts")
            if s < n-m:
                t = (d*(t - h*T[s+1]) + T[s+m+1])%q
            if t<0:
                t = t+q

    return False


T = [1,3,2,4,5,3,6,6]
P = [3,6,6]
RabinKarp(T, P, 10, 3)