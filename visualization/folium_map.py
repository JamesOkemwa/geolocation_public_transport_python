import folium
from folium.plugins import MarkerCluster, LocateControl
import pandas as pd


def load_bus_stops():
    """
    Load bus stops data into a pandas dataframe
    """
    stops_df = pd.read_csv("data/gtfs data/stadtwerke_feed/stops.txt")
    return stops_df


class FoliumMapManager:
    def __init__(self):
        self.munster_coordinates = [51.96, 7.62]
        self.map_instance = None
        self.user_position = None

    def on_location_found(self, e):
        """
        Callback function for when the user location is found
        """
        self.user_position = [e.latitude, e.longitude]
        return self.user_position

    def create_map(self):
        """
        Create folium map centered on Münster and add markers for all bus stops
        """

        if self.map_instance is None:
            self.map_instance = folium.Map(location=self.munster_coordinates, tiles="cartodb positron", zoom_start=12)

            marker_cluster = MarkerCluster(
                name='bus stops',
                overlay=True,
                control=False,
                icon_create_function=None
            )

            stops_df = load_bus_stops()
            for index, bus_stop in stops_df.iterrows():
                bus_stop_coords = [bus_stop['stop_lat'], bus_stop['stop_lon']]
                marker = folium.Marker(location=bus_stop_coords, popup=bus_stop['stop_name'])
                marker_cluster.add_child(marker)

            marker_cluster.add_to(self.map_instance)

            # add geolocation control
            geolocation = LocateControl(auto_start=True)
            self.map_instance.add_child(geolocation)

        return self.map_instance