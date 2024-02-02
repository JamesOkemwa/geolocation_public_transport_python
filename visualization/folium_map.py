import folium

def create_map():
    """
    Create folium map centered on Münster
    """

    m = folium.Map(location=(51.96, 7.62), tiles="cartodb positron", zoom_start=12)

    return m
