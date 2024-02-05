import folium
import pandas as pd


def load_bus_stops():
    """
    Load bus stops data into a pandas dataframe
    """
    stops_df = pd.read_csv("data/gtfs data/stadtwerke_feed/stops.txt")
    return stops_df

def create_map():
    """
    Create folium map centered on Münster and add markers for all bus stops
    """

    m = folium.Map(location=(51.96, 7.62), tiles="cartodb positron", zoom_start=12)

    stops_df = load_bus_stops()
    for index, bus_stop in stops_df.iterrows():
        bus_stop_coords = [bus_stop['stop_lat'], bus_stop['stop_lon']]
        folium.Marker(location=bus_stop_coords, popup=bus_stop['stop_name']).add_to(m)

    return m
