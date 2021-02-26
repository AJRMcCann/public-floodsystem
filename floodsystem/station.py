# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):  # Task 1F part 1 new method
        """Returns True/False if the station
        typical range data is consistent/not"""
        if self.typical_range is None:  # Check if the tuple is empty (no data)
            x = False  # Set x to "False"
        elif self.typical_range[0] < self.typical_range[1]:
            # Check if the High is more than Low
            x = True  # Set x to "True"
        elif self.typical_range[0] > self.typical_range[1]:
            # Check if the Low is more than High
            x = False  # Set x to "False"

        return x  # Set the method output to x (i.e. True or False)

# # Experimental re code, IGNORE
#        x = False   # default to false
#        if (isinstance(self.typical_range, list)    # checks overall list data type
#            and len(self.typical_range) == 2        # checks correct length
#            and isinstance(self.typical_range[1,2], float)  # checks entry data type
#            and self.typical_range[0] < self.typical_range[1]):   # checks consistency
#                x = True
#        return x   # output

    # -------------------------------------------------------------------------
    # EXERCISE 2B
    def relative_water_level(self):     # Task 2B new method
        """Returns latest water level as a fraction of the typical range,
        such that 1.0 corresponds to a typical high and 0.0 to a typical low"""
        levelratio = None   # defaults output to none
        if isinstance(self.latest_level, float) and (
           self.typical_range_consistent()):
            # ^checks if data exists and is consistent
            levelratio = ((self.latest_level - self.typical_range[0]) / (
                self.typical_range[1] - self.typical_range[0]))
            # sets level ratio as output
        return levelratio   # returns output
    # -------------------------------------------------------------------------


def inconsistent_typical_range_stations(stations):
    # Task 1F part 2 new function
    """Returns a list of stations with inconsistent typical range data"""
    outputlist = []  # Initialise output list
    for station in stations:  # Iterate through list of station objects
        if station.typical_range_consistent() is False:
            # Check if that station's data is consistent
            outputlist.append(station)
            # Add station to list if data is inconsistent
    return outputlist
