from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Demonstration Program for Task 2C"""
    stations = build_station_list()     # build station list
    update_water_levels(stations)       # updates water levels
    N = 10     # define how many stations to output

    N_highest_stations = stations_highest_rel_level(stations, N)    # generate names
    output = []    # generate output dictionary

    for i in range(len(stations)):
        if stations[i].name in N_highest_stations:
            temptuple = (stations[i].name, stations[i].relative_water_level())
            # ^creates temporary tuple for storing station name and level
            output.append(temptuple)    # add tuple to output list

    output.sort(key=lambda x: x[1], reverse=1)
    # sort output in descending order

    for i in range(len(output)):
        print("{}, {}".format(output[i][0], output[i][1]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
