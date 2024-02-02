import folium
from folium_map import create_map

def display_map():
    """
    Display an interactive map centered on Münster
    """

    munster_map = create_map()
    munster_map.show_in_browser()

display_map()