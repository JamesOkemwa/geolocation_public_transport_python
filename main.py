from visualization import visualize_map
from geolocation import geolocation

def main():
    # display map
    user_coords = geolocation.get_location_from_ip()

    visualize_map.display_map()


if __name__ == "__main__":
    main()