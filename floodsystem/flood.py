from floodsystem.station import MonitoringStation
# import new MonitoringStation class

# -----------------------------------------------------------------------------
# EXERCISE 2B


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples, each holding i) a station (object) which is
       above the input water level tol; and ii) the relative water level at
       the station"""

    floodstations = []      # creates empty lists for output
    floodlevels = []

    for i in range(len(stations)):      # iterate through stations

        # Data type checks
        if type(stations[i]) is not MonitoringStation:
            raise TypeError("ERROR: Station is not a MonitoringStation")
        if type(stations[i].name) is not str:
            raise TypeError("ERROR: Station 'name' attribute is not a string")
        if type(tol) is not float:
            raise TypeError("ERROR: Tol is not a float")
        if tol < 0 or tol > 1:
            raise ValueError("ERROR: Tol is not between 0.0 and 1.0")

        if (isinstance((stations[i].relative_water_level()), float)
            # ^checks station for valid water level value
                and stations[i].relative_water_level() > tol):
            # ^checks height of water
            floodstations.append(stations[i].name)
            floodlevels.append(stations[i].relative_water_level())
            # ^adds to lists

    floods = []     # create output list
    if ((floodstations is not None)     # checks for station list contents
            and (floodlevels is not None)):   # checks for level list contents
        floods = list(zip(floodstations, floodlevels))  # creates output list
        floods.sort(key=lambda x: x[1], reverse=1)      # sorts in reverse
    return floods
# -----------------------------------------------------------------------------
# EXERCISE 2C


def stations_highest_rel_level(stations, N):
    """Returns a list containing the names of the N stations
    with the highest water level relative to the typical range"""

    names = []     # create list for names
    levels = []     # create list for levels

    for i in range(len(stations)):  # iterate through stations

        if stations[i].relative_water_level() is not None:
            # ^checks for valid relative water level

            names.append(stations[i].name)
            levels.append(stations[i].relative_water_level())
            # ^adds names and levels to respective lists

    combined = list(zip(names, levels))     # combines names and levels
    combined.sort(key=lambda x: x[1], reverse=1)    # sorts in reverse

    output = []   # create output list
    for i in range(N):  # iterate up to N
        output.append(combined[i][0])      # add station name to output

    return output
# -----------------------------------------------------------------------------
