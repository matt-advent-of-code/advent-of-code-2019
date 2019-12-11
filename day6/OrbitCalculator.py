import functools

class Orbit:
    def __init__(self, name, nodes = None):
        self.name = name
        if nodes == None:
            self.nodes = []
        else:
            self.nodes = nodes

class OrbitCalculator:
    def calculate_number_of_orbits(self, center_of_mass):
        return self.calc_number_of_orbits(center_of_mass, 0)

    def calc_number_of_orbits(self, orbit, depth):
        if len(orbit.nodes) == 0:
            return depth
        else:
            number_of_orbits = 0
            for o in orbit.nodes:
                number_of_orbits += self.calc_number_of_orbits(o, depth + 1)
            return depth + number_of_orbits

    def get_paths(self, center_of_mass, dest):
        if center_of_mass.name == dest:
            return [center_of_mass.name]
        else:
            paths = []
            for o in center_of_mass.nodes:
                node_paths = self.get_paths(o, dest)
                if len(node_paths) > 0:
                    if len(node_paths) > 0 and isinstance(node_paths[0], list):
                        paths = [[center_of_mass.name] + p for p in node_paths]
                    elif len(paths) == 0:
                        paths = [center_of_mass.name] + node_paths
                    else:
                        node_paths = [center_of_mass.name] + node_paths
                        paths = [paths] + [node_paths]
            return paths

    def get_min_orbital_transfers(self, orbit, dest1, dest2):
        dest1_paths = self.get_paths(orbit, dest1)
        dest2_paths = self.get_paths(orbit, dest2)

        if not isinstance(dest1_paths[0], list):
            dest1_paths = [dest1_paths]
        if not isinstance(dest2_paths[0], list):
            dest2_paths = [dest2_paths]

        min_distance = len(dest1_paths[0]) + len(dest2_paths[0])
        for dest1_path in dest1_paths:
            for dest2_path in dest2_paths:
                for i in range(len(dest1_path) - 1, -1, -1):
                    for j in range(len(dest2_path) - 1, -1, -1):
                        if dest1_path[i] == dest2_path[j]:
                            distance1 = len(dest1_path) - i - 1
                            distance2 = len(dest2_path) - j - 1
                            distance = distance1 + distance2
                            if distance < min_distance:
                                min_distance = distance

        return min_distance



if __name__ == '__main__':
    f = open("input.txt")
    nodes = {}
    for line in f.readlines():
        node = line.strip("\n").split(")")
        name = node[0]
        child = node[1]
        if child in nodes:
            child_orbit = nodes[child]
        else:
            child_orbit = Orbit(child)
            nodes[child] = child_orbit
        if name in nodes:
            nodes[name].nodes.append(child_orbit)
        else:
            nodes[name] = Orbit(name, [child_orbit])

    orbitCalculator = OrbitCalculator()

    san_orbit = orbitCalculator.get_paths(nodes["COM"], "SAN")[-2]
    you_orbit = orbitCalculator.get_paths(nodes["COM"], "YOU")[-2]
    print orbitCalculator.get_min_orbital_transfers(nodes["COM"], san_orbit, you_orbit)
