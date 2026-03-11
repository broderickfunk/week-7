import math
import unittest
from loader import GeoLoader


class TestLoader(unittest.TestCase):

    def setUp(self):
        """Instantiate a shared GeoLoader for all tests."""
        self.loader = GeoLoader()

    def test_valid_locations(self):
        moma = self.loader.fetch_location_data("Museum of Modern Art")
        self.assertAlmostEqual(moma["latitude"], 40.7618552, places=2)
        self.assertAlmostEqual(moma["longitude"], -73.9782438, places=2)
        self.assertEqual(moma["type"], "museum")

        uss = self.loader.fetch_location_data(
            "USS Alabama Battleship Memorial Park"
        )
        self.assertAlmostEqual(uss["latitude"], 30.684373, places=2)
        self.assertAlmostEqual(uss["longitude"], -88.015316, places=2)
        self.assertEqual(uss["type"], "park")

    def test_invalid_location(self):
        result = self.loader.fetch_location_data("asdfqwer1234")
        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(math.isnan(result["latitude"]))
        self.assertTrue(math.isnan(result["longitude"]))
        self.assertTrue(math.isnan(result["type"]))


if __name__ == "__main__":
    unittest.main()