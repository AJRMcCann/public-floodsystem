from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    """Demonstration Program for Task 2B"""

    stations = build_station_list()     # build stations list
    update_water_levels(stations)       # updates water levels
    threshold = 0.8     # define threshold

    highstations = stations_level_over_threshold(stations, threshold)
    # ^build high station list

    if highstations is None:    # checks list for contents
        print("No stations above threshold of {}".format(threshold))
    else:
        for i in range(len(highstations)):      # iterate through list
            print("{}, {}".format(highstations[i][0], highstations[i][1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
