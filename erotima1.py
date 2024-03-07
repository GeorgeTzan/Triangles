import random
import statistics
import itertools
from utils import *


def main():
    points = [
        (random.randint(-100, 100), random.randint(-100, 100)) for _ in range(100)
    ]

    triangles = []

    for triangle in itertools.combinations(points, 3):
        triangles.append(triangle)

    valid_triangles = []
    triangle_areas = []
    for triangle in triangles:
        area = triangle_area(triangle[0], triangle[1], triangle[2])
        if area > 1e-6:
            triangle_areas.append(area)
            valid_triangles.append(triangle)

    print(f"Valid Trigwna:{round(len(valid_triangles),2)}")
    meanFunct = mean(triangle_areas)
    medianFunct = median(triangle_areas)
    stdevFunct = stdev(triangle_areas)

    meanStats = statistics.mean(triangle_areas)
    medianStats = statistics.median(triangle_areas)
    stdevStats = statistics.stdev(triangle_areas)

    print("Results using custom functions:")
    print(
        f"Mean area: {meanFunct:.2f}\nMedian area: {medianFunct:.2f}\nSt deviation areas: {stdevFunct:.2f}"
    )

    print("Results using Module statistics:")
    print(
        f"Mean area: {meanStats:.2f}\nMedian area: {medianStats:.2f}\nSt deviation areas: {stdevStats:.2f}"
    )


if __name__ == "__main__":
    main()
