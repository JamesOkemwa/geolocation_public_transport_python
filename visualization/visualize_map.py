import folium
from .folium_map import FoliumMapManager

folium_map = FoliumMapManager()

def display_map():
    """
    Display an interactive map centered on Münster
    """

    munster_map = folium_map.create_map()
    munster_map.show_in_browser()