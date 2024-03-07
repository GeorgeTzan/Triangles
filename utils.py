import math


def measure_distance(point_one, point_two):
    x1, y1 = point_one
    x2, y2 = point_two
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def triangle_area(a, b, c):
    side1 = measure_distance(a, b)
    side2 = measure_distance(b, c)
    side3 = measure_distance(a, c)

    if ((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) == 0:
        return 0

    s = (side1 + side2 + side3) / 2

    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def mean(values):
    return sum(values) / len(values)


def median(values):
    valuesSorted = sorted(values)
    n = len(values)
    if n % 2 == 0:
        return (valuesSorted[n // 2] + valuesSorted[n // 2 - 1]) / 2
    else:
        return valuesSorted[n // 2]


def valuesRange(values):
    return max(values) - min(values)


def stdev(values):
    means = mean(values)
    variance = sum((x - means) ** 2 for x in values) / len(values)
    return math.sqrt(variance)
