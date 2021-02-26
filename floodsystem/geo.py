# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
from floodsystem.station import MonitoringStation
# import new MonitoringStation class
import numpy as np  # always good to have numpy in case # noqa
from haversine import haversine, Unit   # noqa
# import premade haversine function rather than try to build one using numpy
import plotly.express as px


def stations_by_distance(stations, p):  # 1B task
    """This function returns a list of tuples
    consisting of a station and its distance
    from a given coordinate "p". This list is
    sorted by that distance
    The input "stations" should be a list of stations of
    type MonitoringStation. Coordinate "p" should be a tuple
    in the form (latitude, longitude).
    """
    unsortedlist = []  # create empty list

    for i in range(len(stations)):
        if type(stations[i]) is MonitoringStation:
            pass
        else:
            raise TypeError("Station object must be"
                            " of the type MonitoringStation")
            # ensure that the data is given in the correct form
        if type(stations[i].name) is str:
            pass
        else:
            raise TypeError("Station name must be of the type string")
            # ensure that the data is given in the correct form
        if type(stations[i].coord) is tuple:
            pass
        else:
            raise TypeError("Station coords must be of the type tuple")
            # ensure that the data is given in the correct form

        stationdistance = haversine(stations[i].coord, p, unit="km")
        # use haversine function to find distance for
        # that station (in kilometres as specified)
        outputtuple = (stations[i], stationdistance)
        # create an output tuple with the station name and the
        # newly found distance from p
        unsortedlist.append(outputtuple)
        # add the output tuple to the unsorted list

    sortedlist = []  # create empty output list
    sortedlist = sorted_by_key(unsortedlist, 1)
    # sort the unsorted list by distance using the function from utils

    return sortedlist


def stations_within_radius(stations, centre, r):  # 1C task
    """This function returns an unsorted list of stations within a radius "r" of a
    coordinate centre "centre" (longitude and latitude).
    The radius is in kilometres.
    The input "stations" should be a list of stations
    of type MonitoringStation.
    "centre" should be given as a tuple in the form (latitude, longitude).
    """
    outputlist = []  # Initialise empty output list
    for i in range(len(stations)):  # Iterate through the list of stations
        if type(stations[i]) is MonitoringStation:
            pass
        else:
            raise TypeError("Station object must be"
                            "of the type MonitoringStation")
            # ensure that the data is given in the correct form
        if type(stations[i].name) is str:
            pass
        else:
            raise TypeError("Station name must be of the type string")
            # ensure that the data is given in the correct form

        if type(stations[i].coord) is tuple:
            pass
        else:
            raise TypeError("Station coords must be of the type tuple")
            # ensure that the data is given in the correct form

        stationdistance = haversine(stations[i].coord, centre, unit="km")
        # use haversine function to find distance for
        # that station (in kilometres as specified)

        if stationdistance < 0:  # Checking value of station distance
            raise ValueError("Error, distance cannot be less than zero")

        elif stationdistance > 20000:  # Checking value of station distance
            raise ValueError("Error, distance cannot be more than"
                             "half of the circumference of the Earth")

        elif stationdistance < r:
            # Check if the station distance is less than the given radius
            outputlist.append(stations[i])  # Add that station to the list

        else:
            pass

    return outputlist

# ---------------------------------------------------------------------------

# EXERCISE 1D

# Part 1


def rivers_with_stations(stations):
    """Returns a set containing all rivers with stations located on them"""

    rivers = set()      # Create empty set
    for i in range(len(stations)):   # Iterate through list of stations

        # Data type checks
        if type(stations[i]) is MonitoringStation:
            pass
        else:
            raise TypeError("ERROR: Station is not a MonitoringStation")
        if type(stations[i].river) is str:
            pass
        else:
            raise TypeError("ERROR: Station 'river' attribute is not a string")

        rivers.add(stations[i].river)   # Add rivers to set

    return rivers   # Returns set of rivers


# Part 2
def stations_by_river(stations):
    """Returns a dictionary mapping river names (key)
       to a list of stations (object)"""

    rivers_stations_dict = {}   # Create empty dictionary

    for i in range(len(stations)):   # Iterate through list of stations

        # Data type checks
        if type(stations[i]) is MonitoringStation:
            pass    # Checks if stations are correct class
        else:
            raise TypeError("ERROR: Station is not a MonitoringStation")
        if type(stations[i].name) is str:  # Checks if name is string
            pass
        else:
            raise TypeError("ERROR: Station 'name' attribute is not a string")
        if type(stations[i].river) is str:  # Checks if river is string
            pass
        else:
            raise TypeError("ERROR: Station 'river' attribute is not a string")

        if not stations[i].river in rivers_stations_dict:
            # Checks if river is not in dictionary
            rivers_stations_dict[stations[i].river] = []
            # Adds river to dictionary with blank list
        if not stations[i].name in rivers_stations_dict:
            rivers_stations_dict[stations[i].river].append(stations[i].name)
            # Adds station name to object list

    return rivers_stations_dict   # Returns dictionary of rivers-stations


# ---------------------------------------------------------------------------

# EXERCISE E

def rivers_by_station_number(stations, N):
    """Determines the top N rivers by number of stations"""

    riverslist = []   # creates empty list
    riversdict = {}   # Create empty dictionary

    for i in range(len(stations)):   # Iterate through list of stations

        # Data type checks
        if type(stations[i]) is MonitoringStation:
            pass    # Checks if stations are correct class
        else:
            raise TypeError("ERROR: Station is not a MonitoringStation")
        if type(stations[i].name) is str:  # Checks if name is string
            pass
        else:
            raise TypeError("ERROR: Station 'name' attribute is not a string")
        if type(stations[i].river) is str:  # Checks if river is string
            pass
        else:
            raise TypeError("ERROR: Station 'river' attribute is not a string")

        if not stations[i].river in riversdict:
            # Checks if river is not in dictionary
            riversdict[stations[i].river] = 0
            # Adds river to dictionary with zero counter
        riversdict[stations[i].river] += 1        # Adds one to counter

    statcount = sorted(riversdict.values(), reverse=True)
    # create list of station numbers from highest to lowest
    for i in range(N):      # iterate through first N values
        for riv, count in riversdict.items():
            # iterate through dictionary of rivers-station numbers
            if (count == statcount[i]) and (riv not in riverslist):
                # checks if dictionary entry has been entered
                riverslist.append(riv)  # appends river name and no. stations
                riverslist.append(count)
    riverslistpaired = [(riverslist[i], riverslist[i + 1])
                        for i in range(0, len(riverslist), 2)]
    # pairs into tuples

    return riverslistpaired       # returns output


# ------------------------------------------------------------------------------


def plot_on_map(list_of_stations, map_style=1):
    # Mapping Extension Function for Milestone 1
    """Plots a list of stations on a map using Plotly Express and Mapbox.
    The "list_of_stations" should be a list of stations
    of type MonitoringStation.
    Styles of Maps that don't need a mapbox token are: "Open Street Map"(0),
    "Carto Positron"(1), "Carto Darkmatter"(2), "Stamen Terrain"(3),
    "Stamen Toner"(4), and "Stamen Watercolour"(5) """

    style_dict = {0: "open-street-map",
                  1: "carto-positron",
                  2: "carto-darkmatter",
                  3: "stamen-terrain",
                  4: "stamen-toner",
                  5: "stamen-watercolour"}
    # Dictionary of mapbox styles that don't require a token

    # Initialise Lists
    name_list = []
    coord_list = []
    lat_list = []
    lon_list = []

    for station in list_of_stations:  # Iterate through list of stations
        name_list.append(station.name)  # Add station name to list of names
        coord_list.append(station.coord)
        # Add station coords to list of coords
        lat_list.append(station.coord[0])
        # Add station latitude to list of latitudes
        lon_list.append(station.coord[1])
        # Add station longitude to list of longitudes
    name_coord_dict = {tuple(name_list): tuple(coord_list)}
    # Create dictionary of station names and coords

    # px.set_mapbox_access_token("""pk.eyJ1IjoiYWpybWNjYW5uIiwiYSI6I
    # mNra2p6N3IwOTIzdTcycHF1MHR5bTg3amUifQ.Hum-h329Fs-0LGSOEhhj0g""")
    # Token not required for this mapbox style, so commented out to avoid
    # errors around invalid tokens

    fig = px.scatter_mapbox(name_coord_dict, lat=lat_list,
                            lon=lon_list, hover_name=name_list)
    # Use Plotly Express to create the figure

    fig.update_layout(mapbox_style=style_dict[map_style])
    # Use the chosen mapbox style

    fig.show()  # Display the figure (in new tab)
