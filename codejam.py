import time
count = int(raw_input())

def diff(teama, teamb, remaining):
    if len(remaining) == 0:
        return abs(teama-teamb)
    return min(diff(teamb + remaining[i], teama, remaining[:i] + remaining[i+1:]) for i in range(len(remaining)))

t = time.time()
for i in range(count):
    numbers = map(int, raw_input().split())
    print "Case #%d: %d" % (i+1, diff(0,0,numbers[1:]))
