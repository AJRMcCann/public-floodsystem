# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the stationdata module"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels


def test_build_station_list():

    # Build list of stations
    stations = build_station_list()

    # Find station 'Cam'
    for station in stations:
        if station.name == 'Cam':
            station_cam = station
            break

    # Assert that station is found
    assert station_cam

    # Fetch data over past 2 days
    dt = 2
    dates2, levels2 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates2) == len(levels2)

    # Fetch data over past 10 days
    dt = 10
    dates10, levels10 = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    assert len(dates10) == len(levels10)
    assert len(dates10) > len(levels2)


# ----------------------------------------
# 2G TESTING RIG
stations = build_station_list()  # build station list
update_water_levels(stations)  # update water levels
teststation = "Hayes Basin"
examplestation = "Redhill"

for station in stations:    # iterate through stations
    if (station.name == teststation) or (station.name == examplestation):      # find example stations
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))    # fetch date/level data # noqa
        print("\n---------------------------------------------------------------------------------------"
              "\n{} \n\n{} \n\n{}".format(station.name, dates, levels))

        output = []        # initialise output
        for i in range(3):      # iterate through first 3 entries
            entry = "Date: {}, Level: {}".format(dates[i], levels[i])
            output.append(entry)        # add relevant data to output
        print("\n{}".format(station.name))
        for i in output:
            print(i)     # print outputs
# ----------------------------------------
