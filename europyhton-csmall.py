import sys

n = int(sys.stdin.readline())

for c in xrange(n):
    m = int(sys.stdin.readline())
    incompatible = {}
    for p in xrange(m):
        a, b = sys.stdin.readline().strip().split(" ")
        try:
            incompatible[a].append(b)
        except KeyError:
            incompatible[a] = [b]
        try:
            incompatible[b].append(a)
        except KeyError:
            incompatible[b] = [a]

    color = {}
    bad = [False]
    def fill(x, c):
        cx = color.get(x)
        if cx == 3 - c:
            bad[0] = True
            return
        elif cx is None:
            color[x] = c
            for y in incompatible[x]:
                fill(y, 3 - c)
                if bad[0]: return
    for a in incompatible.keys():
        if color.get(a) is None:
            fill(a, 1)
            if bad[0]:
                break
    print "Case #%i: %s" % (c+1, ["Yes", "No"][bad[0]])
