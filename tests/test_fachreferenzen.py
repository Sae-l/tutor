"""Sollwerte der selbst erstellten Abnahmeaufgaben; keine Modellbewertung."""
import math
import unittest


class FachreferenzenTests(unittest.TestCase):
    def test_quadratische_gleichung_und_definitionsbereich(self):
        roots = [(5 + sign * math.sqrt(25 - 24)) / 2 for sign in (-1, 1)]
        self.assertEqual(roots, [2, 3])
        for x in roots:
            self.assertEqual(x * x - 5 * x + 6, 0)
        candidates = [0, 3]  # Nach Quadrieren von sqrt(x + 1) = x - 1.
        self.assertEqual([x for x in candidates if x >= 1 and math.sqrt(x + 1) == x - 1], [3])

    def test_freier_fall_energie_und_kinematik(self):
        g, h, m = 9.81, 5.00, 2
        time = math.sqrt(2 * h / g)
        newton = g * time
        energy = math.sqrt(2 * m * g * h / m)
        self.assertAlmostEqual(newton, energy)
        self.assertAlmostEqual(energy, 9.904544411531507)

    def test_schaltung_knoten_und_leistung(self):
        voltage, r1, r2, r3 = 12, 2000, 3000, 6000
        parallel = 1 / (1 / r2 + 1 / r3)
        node_voltage = voltage * parallel / (r1 + parallel)
        nodal = (voltage / r1) / (1 / r1 + 1 / r2 + 1 / r3)
        self.assertAlmostEqual(node_voltage, nodal)
        self.assertAlmostEqual(node_voltage, 6)
        currents = ((voltage - node_voltage) / r1, node_voltage / r2, node_voltage / r3)
        for actual, expected in zip(currents, (0.003, 0.002, 0.001)):
            self.assertAlmostEqual(actual, expected)
        self.assertAlmostEqual(currents[0], currents[1] + currents[2])
        self.assertAlmostEqual(voltage * currents[0], sum(i * i * r for i, r in zip(currents, (r1, r2, r3))))

    def test_balken_kraft_und_moment(self):
        load, length, position = 600, 4, 1
        by = load * position / length
        ay = load - by
        self.assertEqual((ay, by), (450, 150))
        self.assertEqual(ay + by - load, 0)
        self.assertEqual(ay * length - load * (length - position), 0)


if __name__ == "__main__":
    unittest.main()
