class ClosestIntersectionFinder:
    def __init__(self, rows, cols, central_port):
        self.wire1 = self.__init_wire(cols, rows)
        self.wire2 = self.__init_wire(cols, rows)
        self.central_port = central_port
        self.intersections = []

    def __init_wire(self, cols, rows):
        return [[0 for i in range(cols)] for j in range(rows)]

    def draw_wire1(self, path):
        self.__draw_wire(self.wire1, path)

    def draw_wire2(self, path):
        self.__draw_wire(self.wire2, path)

    def calculate_intersections(self):
        for i in range(0, len(self.wire1)):
            for j in range(0, len(self.wire1[i])):
                if self.wire1[i][j] > 0 and self.wire2[i][j] > 0:
                    self.intersections.append((i, j))

    def calculate_manhattan_distance(self, index1, index2):
        return abs(index1[0] - index2[0]) + abs(index1[1] - index2[1])

    def calculate_shortest_distance(self):
        self.calculate_intersections()
        intersection = self.intersections[0]
        shortest_intersection = self.wire1[intersection[0]][intersection[1]] + self.wire2[intersection[0]][intersection[1]]
        for intersection in self.intersections:
            distance = self.wire1[intersection[0]][intersection[1]] + self.wire2[intersection[0]][intersection[1]]
            if distance < shortest_intersection:
                shortest_intersection = distance
        return shortest_intersection

    def __draw_wire(self, wire, path):
        index = self.central_port
        distanced_travled = 0
        for operation in path:
            direction = operation[0]
            length = int(operation[1:])
            for i in range(length, 0, -1):
                if direction == "R":
                    index = (index[0], index[1] + 1)
                elif direction == "U":
                    index = (index[0]-1, index[1])
                elif direction == "D":
                    index = (index[0]+1, index[1])
                else:
                    index = (index[0], index[1] - 1)
                distanced_travled += 1
                wire[index[0]][index[1]] = distanced_travled


if __name__ == '__main__':
   closest_intersection_finder = ClosestIntersectionFinder(20000, 20000, (10000, 10000))
   f = open("input.txt")
   wire1_path = f.readline().split(",")
   wire2_path = f.readline().split(",")
   f.close()
   closest_intersection_finder.draw_wire1(wire1_path)
   closest_intersection_finder.draw_wire2(wire2_path)
   print closest_intersection_finder.calculate_shortest_distance()



