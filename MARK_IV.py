import detect_video
import detect_video_e
import detect_video_s
import detect_video_w
north = detect_video.car()
#east = detect_video_e.car()
#west = detect_video_w.car()
south = detect_video_s.car()
east = detect_video_e.car()
west = detect_video_w.car()

print(north, south, east, west)

#q = d

def y_ratio(q1, q2, q3, q4):
    sf = [1850, 1890, 1950, 2250, 2250, 2900]
    y1, y2, y3, y4 = q1 / sf[2] * 40, q2 / sf[2] * 40, q3 / sf[2] * 40, q4 / sf[2] * 40
    return y1, y2, y3, y4


def lost_time(n):
    return 2 * n + 3


def cycle_time(q, n):
    y1, y2, y3, y4 = y_ratio(q[0], q[1], q[2], q[3])
    l = lost_time(n)
    y = y1 + y2 + y3 + y4
    c_time = (1.5 * l + 5) / (1 - y)
    return c_time


def green_light(q, n):
    y1, y2, y3, y4 = y_ratio(q[0], q[1], q[2], q[3])
    l = lost_time(n)
    c = cycle_time(q, n)
    y = y1 + y2 + y3 + y4
    g1, g2, g3, g4 = (y1 / y) * (c - l), (y2 / y) * (c - l), (y3 / y) * (c - l), (y4 / y) * (c - l),
    g1, g2, g3, g4 = str(abs(g1)), str(abs(g2)), str(abs(g3)), str(abs(g4))
    print("North Phase " + g1 + "\nEast Phase  " + g2 + "\nWest Phase  " + g3 + "\nSouth Phase " + g4)


q = [north, south, east, west]
print("Cycle Time\t" + str(abs(cycle_time(q, 4))))
print(green_light(q, 4))


