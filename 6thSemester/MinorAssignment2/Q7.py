import math
import bisect

def find_antipodal_points(points):
    angles = [math.atan2(y, x) for x, y in points]
    angles.sort()
    for angle in angles:
        antipodal_angle = angle + math.pi
        if antipodal_angle > math.pi:
            antipodal_angle -= 2 * math.pi  # Ensure it's within [-π, π]
        idx = bisect.bisect_left(angles, antipodal_angle)
        if idx < len(angles) and angles[idx] == antipodal_angle:
            return True
    return False

points = [(1, 0), (-1, 0), (0, 1), (0, -1)]
print(find_antipodal_points(points))