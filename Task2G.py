from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level     # noqa

from floodsystem.analysis import risk_by_gradients
import matplotlib.pyplot as plt     # requirement # noqa

# --------------------------------------------------------------------------------------------------------
# CODE START

stations = build_station_list()  # build station list
update_water_levels(stations)  # update water levels

N = 3      # how many stations to build functions for
workstations = stations_highest_rel_level(stations, N)  # creates list of station names

# alternative implementation, consider all stations above threshold
# threshold = 1   # sets threshold
# highstations = stations_level_over_threshold(stations, threshold)   # calculate stations above threshold
# workstations = []   # initialise list for station names
# for i in highstations:  # iterate through highstations
#    workstations.append(highstations[0])    # adds station names

riverfunctions = []     # create lists for river data
dt = 5     # how many days back to check
p = 2      # polynomial order to produce, must be greater than 2

for station in stations:  # iterate through stations

    if station.name in workstations:    # check if station is in desired check list
        # print("\n{}:".format(station.name))   # print station name for testing

        risk = risk_by_gradients(station, dt, p)   # calculate risk by gradient

        entry = [station.name, risk]    # initialise output list
        riverfunctions.append(entry)       # adds to master list

for i in riverfunctions:    # for testing
    print(i)
