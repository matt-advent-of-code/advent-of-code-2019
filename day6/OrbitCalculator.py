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
    print orbitCalculator.calculate_number_of_orbits(nodes["COM"])
