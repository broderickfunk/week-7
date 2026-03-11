'''
Script to load geographical data into a pandas DataFrame using a Python class.
'''

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import pandas as pd


class GeoLoader:
    """Loads geographical data into a pandas DataFrame."""

    def __init__(self, agent='h501-student'):
        """
        Initialize the GeoLoader with a Nominatim geolocator.

        Parameters
        ----------
        agent : str, optional
            User agent name for Nominatim, by default 'h501-student'
        """
        self.geolocator = Nominatim(user_agent=agent)

    def fetch_location_data(self, loc):
        """
        Fetch geo data for a single location string.

        Parameters
        ----------
        loc : str
            The location name to look up.
        """
        try:
            location = self.geolocator.geocode(loc)
        except (GeocoderTimedOut, GeocoderServiceError):
            location = None

        if location is None:
            return {
                "location": loc,
                "latitude": float("nan"),
                "longitude": float("nan"),
                "type": float("nan")
            }

        return {
            "location": loc,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "type": location.raw.get("type")
        }

    def build_geo_dataframe(self, locations):
        """
        Build a pandas DataFrame of geo data for a list of location strings.

        Parameters
        ----------
        locations : list of str
            Location names to look up.
        """
        geo_data = [self.fetch_location_data(loc) for loc in locations]
        return pd.DataFrame(geo_data)


if __name__ == "__main__":
    loader = GeoLoader()

    locations = [
        "Museum of Modern Art",
        "iuyt8765(*&)",
        "Alaska",
        "Franklin's Barbecue",
        "Burj Khalifa"
    ]

    df = loader.build_geo_dataframe(locations)
    df.to_csv("./geo_data.csv")