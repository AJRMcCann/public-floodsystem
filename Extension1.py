from floodsystem.stationdata import build_station_list
from floodsystem.geo import plot_on_map


def run():
    """Demonstration Program for Milestone 1 Mapping Extension"""
    list_of_stations = build_station_list()  # Create list of stations
    return(plot_on_map(list_of_stations, 1))
    # Use plot_on_map function to display figure


if __name__ == "__main__":
    print("***Milestone 1 Mapping Extension:"
          "CUED Part IA Flood Warning System ***")
    run()
