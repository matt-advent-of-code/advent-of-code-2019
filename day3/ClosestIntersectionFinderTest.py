import unittest

from day3.ClosestIntersectionFinder import ClosestIntersectionFinder


class MyTestCase(unittest.TestCase):
    def test_init_grid(self):
        expected_grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (0,4))

        self.assertEqual(expected_grid, intersection_finder.wire1)
        self.assertEqual(expected_grid, intersection_finder.wire2)
        self.assertEqual(intersection_finder.central_port, (0,4))

    def test_draw_wire1_right(self):
        expected_wire1= [[0, 0, 0, 0],
                         [0, 1, 2, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire2 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (1, 0))
        intersection_finder.draw_wire1(["R2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire2_right(self):
        expected_wire2= [[0, 0, 0, 0],
                         [0, 1, 2, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire1 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (1, 0))
        intersection_finder.draw_wire2(["R2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire1_left(self):
        expected_wire1= [[0, 0, 0, 0],
                         [0, 2, 1, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire2 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (1, 3))
        intersection_finder.draw_wire1(["L2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)


    def test_draw_wire2_left(self):
        expected_wire2= [[0, 0, 0, 0],
                         [0, 2, 1, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire1 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (1, 3))
        intersection_finder.draw_wire2(["L2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire1_up(self):
        expected_wire1= [[0, 0, 0, 0],
                         [2, 0, 0, 0],
                         [1, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire2 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (3, 0))
        intersection_finder.draw_wire1(["U2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire2_up(self):
        expected_wire2= [[0, 0, 0, 0],
                         [2, 0, 0, 0],
                         [1, 0, 0, 0],
                         [0, 0, 0, 0]]

        expected_wire1 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (3, 0))
        intersection_finder.draw_wire2(["U2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire1_down(self):
        expected_wire1 = [[0, 0, 0, 0],
                          [1, 0, 0, 0],
                          [2, 0, 0, 0],
                          [0, 0, 0, 0]]

        expected_wire2 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (0, 0))
        intersection_finder.draw_wire1(["D2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_wire2_down(self):
        expected_wire2 = [[0, 0, 0, 0],
                          [1, 0, 0, 0],
                          [2, 0, 0, 0],
                          [0, 0, 0, 0]]

        expected_wire1 = [[0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0],
                          [0, 0, 0, 0]]
        intersection_finder = ClosestIntersectionFinder(4, 4, (0, 0))
        intersection_finder.draw_wire2(["D2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)
        self.assertEqual(expected_wire2, intersection_finder.wire2)

    def test_draw_multi(self):
        expected_wire1 = [[0, 0, 0, 0],
                          [1, 0, 0, 0],
                          [2, 3, 4, 0],
                          [0, 0, 0, 0]]

        intersection_finder = ClosestIntersectionFinder(4, 4, (0, 0))
        intersection_finder.draw_wire1(["D2", "R2"])

        self.assertEqual(expected_wire1, intersection_finder.wire1)

    def test_get_intersections(self):
        intersection_finder = ClosestIntersectionFinder(4, 4, (0, 0))
        intersection_finder.wire1 = [[1, 1, 1, 1],
                          [0, 0, 0, 0],
                          [1, 1, 1, 1],
                          [0, 0, 0, 0]]

        intersection_finder.wire2 = [[1, 0, 0, 0],
                          [1, 0, 0, 0],
                          [1, 0, 0, 0],
                          [1, 0, 0, 0]]

        expected_intersections = [(0,0), (2,0)]
        intersection_finder.calculate_intersections()
        self.assertEqual(expected_intersections, intersection_finder.intersections)


    def test_get_manhattan_distance(self):
        intersection_finder = ClosestIntersectionFinder(10, 10, (8, 1))
        distance = intersection_finder.calculate_manhattan_distance((8, 1), (5, 4))
        expected_distance = 6
        self.assertEqual(expected_distance, distance)

    def test_get_shortest_distance(self):
        intersection_finder = ClosestIntersectionFinder(1000, 1000, (8, 1))
        intersection_finder.draw_wire1(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])
        intersection_finder.draw_wire2(["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"])
        expected_distance = 610
        distance = intersection_finder.calculate_shortest_distance()
        self.assertEqual(expected_distance, distance)

    def test_get_shortest_distance_example_2(self):
        intersection_finder = ClosestIntersectionFinder(1000, 1000, (500, 500))
        intersection_finder.draw_wire1(["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"])
        intersection_finder.draw_wire2(["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"])
        expected_distance = 410
        distance = intersection_finder.calculate_shortest_distance()
        self.assertEqual(expected_distance, distance)




if __name__ == '__main__':
    unittest.main()
