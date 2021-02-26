from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river


def run():
    """Task 1D"""

    stations = build_station_list()     # Build list of stations

    # Part 1
    rivers = rivers_with_stations(stations)   # Uses function from 1D.1
    sortedrivers = sorted(rivers)     # creates sorted set
    tenrivers = []        # creates empty list for 10 rivers
    for i in range(10):     # iterates through first 10 values
        tenrivers.append(sortedrivers[i])       # adds from sorted river list
    print("Part 1\n-------\n{0} stations on rivers."
          "\nFirst 10 Alphabetically:\n{1}"
          .format(len(rivers), tenrivers))   # prints output

    # Part 2
    riverstations = stations_by_river(stations)     # Uses function from 1D.2
    Aire = sorted(riverstations['River Aire'])      # Creates sorted list
    Cam = sorted(riverstations['River Cam'])              # ""
    Thames = sorted(riverstations['River Thames'])        # ""
    print("\nPart 2\n-------\nRiver Aire Stations: \n{0}"
          "\n\nRiver Cam Stations: \n{1}"
          "\n\nRiver Thames Stations: \n{2}"
          .format(Aire, Cam, Thames))   # prints output


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
