import unittest
from rust_core_test import HyperBlackHole4D

class TestHyperBlackHole4D(unittest.TestCase):
    def test_zero_mass(self):
        bh = HyperBlackHole4D(0.0)
        self.assertEqual(bh.compute_event_horizon(), 0.0)
        self.assertEqual(bh.compute_hawking_temperature(), 0.0)

    def test_negative_mass(self):
        bh = HyperBlackHole4D(-5.0)
        with self.assertRaises(ValueError):
            bh.compute_event_horizon()

    def test_positive_mass(self):
        bh = HyperBlackHole4D(1e15)
        rh = bh.compute_event_horizon()
        self.assertGreater(rh, 0.0)
        temp = bh.compute_hawking_temperature()
        self.assertGreater(temp, 0.0)

if __name__ == '__main__':
    unittest.main()
