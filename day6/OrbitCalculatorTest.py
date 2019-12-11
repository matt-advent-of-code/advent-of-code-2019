import unittest

from day6.OrbitCalculator import Orbit, OrbitCalculator


class MyTestCase(unittest.TestCase):
    def test_orbit(self):
        orbit = Orbit("COM")
        self.assertEqual("COM", orbit.name)
        self.assertEqual([], orbit.nodes)

    def test_calculate_orbit(self):
        orbit = Orbit("COM")
        orbit.nodes = [
            Orbit("B", [
                Orbit("G", [
                    Orbit("H")
                ]),
                Orbit("C", [
                    Orbit("D", [
                        Orbit("I"),
                        Orbit("E", [
                            Orbit("F"),
                            Orbit("J", [
                                Orbit("K", [
                                    Orbit("L")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ]

        orbitCalculator = OrbitCalculator()
        self.assertEqual(42, orbitCalculator.calculate_number_of_orbits(orbit))

    def test_calculate_paths(self):
        orbit = Orbit("COM")
        orbit.nodes = [
            Orbit("B", [
                Orbit("G", [
                    Orbit("H")
                ]),
                Orbit("C", [
                    Orbit("D", [
                        Orbit("I"),
                        Orbit("E", [
                            Orbit("F"),
                            Orbit("J", [
                                Orbit("K", [
                                    Orbit("L")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ]
        expected_path = ["COM", "B", "C", "D", "I"]
        orbitCalculator = OrbitCalculator()
        self.assertEqual(expected_path, orbitCalculator.get_paths(orbit, "I"))


    def test_calculate_multiple_paths(self):
        orbit = Orbit("COM")
        orbit.nodes = [
            Orbit("B", [
                Orbit("G", [
                    Orbit("I")
                ]),
                Orbit("C", [
                    Orbit("D", [
                        Orbit("I"),
                        Orbit("E", [
                            Orbit("F"),
                            Orbit("J", [
                                Orbit("K", [
                                    Orbit("L")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ]
        expected_path = [["COM", "B", "G", "I"], ["COM", "B", "C", "D", "I"]]
        orbitCalculator = OrbitCalculator()
        self.assertEqual(expected_path, orbitCalculator.get_paths(orbit, "I"))

    def test_min_orbit(self):
        orbit = Orbit("COM")
        orbit.nodes = [
            Orbit("B", [
                Orbit("G", [
                    Orbit("H")
                ]),
                Orbit("C", [
                    Orbit("D", [
                        Orbit("I"),
                        Orbit("E", [
                            Orbit("F"),
                            Orbit("J", [
                                Orbit("K", [
                                    Orbit("L")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ]
        orbitCalculator = OrbitCalculator()
        self.assertEqual(4, orbitCalculator.get_min_orbital_transfers(orbit, "K", "I"))


if __name__ == '__main__':
    unittest.main()
