import itertools
import unittest
from utils import *

points = []
with open("points.txt", "r") as file:
    for line in file:
        x, y = map(int, line.strip().split())
        points.append((x, y))

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

print(f"Valid Triangles: {len(valid_triangles)}")
meanFunct = mean(triangle_areas)
medianFunct = median(triangle_areas)
stdevFunct = stdev(triangle_areas)

print("Results using custom functions:")
print(
    f"Mean area: {meanFunct:.2f}\nMedian area: {medianFunct:.2f}\nSt deviation areas: {stdevFunct:.2f}"
)


class TestTriangleAreas(unittest.TestCase):
    def test_values(self):
        self.assertEqual(len(triangle_areas), 161671)
        self.assertAlmostEqual(meanFunct, 3206.86, places=2)
        self.assertAlmostEqual(medianFunct, 2392.50, places=2)
        self.assertAlmostEqual(stdevFunct, 2843.23, places=2)


unittest.main()
