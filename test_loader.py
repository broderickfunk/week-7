import unittest
import pandas as pd
from loader import *

class TestLoader(unittest.TestCase):
    def test_valid_locations(self):
        geolocator = get_geolocator()

        museum = fetch_location_data(geolocator, "Museum of Modern Art")
        park = fetch_location_data(geolocator, "USS Alabama Battleship Memorial Park")

        self.assertEqual(museum["location"], "Museum of Modern Art")
        self.assertAlmostEqual(museum["latitude"], 40.7618552, places=2)
        self.assertAlmostEqual(museum["longitude"], -73.9782438, places=2)
        self.assertEqual(museum["type"], "museum")

        self.assertEqual(park["location"], "USS Alabama Battleship Memorial Park")
        self.assertAlmostEqual(park["latitude"], 30.684373, places=2)
        self.assertAlmostEqual(park["longitude"], -88.015316, places=2)
        self.assertEqual(park["type"], "park")

    def test_invalid_location(self):
        geolocator = get_geolocator()
        result = fetch_location_data(geolocator, "asdfqwer1234")

        self.assertEqual(result["location"], "asdfqwer1234")
        self.assertTrue(pd.isna(result["latitude"]))
        self.assertTrue(pd.isna(result["longitude"]))
        self.assertTrue(pd.isna(result["type"]))

def test_invalid_location(self):
    geolocator = get_geolocator()
    result = fetch_location_data(geolocator, "asdfqwer1234")

    self.assertEqual(result["location"], "asdfqwer1234")
    self.assertTrue(pd.isna(result["latitude"]))
    self.assertTrue(pd.isna(result["longitude"]))
    self.assertTrue(pd.isna(result["type"]))

if __name__ == "__main__":
    unittest.main()
