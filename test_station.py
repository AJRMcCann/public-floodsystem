# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station submodule"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():
    """Test for the create_monitoring_station function, by
    creating an example station and ensuring its attributes
    are correct.
    """
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent():
    """Test of the typical_range_consistent function by creating 3
    example stations with consistent range, inconsistent range, and no
    range respectively, and ensuring the function gives the correct output.
    """
    # Create a consistent station (using same data as above)
    s1_id = "test-s1-id"
    m1_id = "test-m1-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    river1 = "River X"
    town1 = "My Town"
    s1 = MonitoringStation(s1_id, m1_id, label1, coord1, trange1, river1, town1)

    # Create another inconsistent station
    s2_id = "test-s2-id"
    m2_id = "test-m2-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (2.3, -3.4445)
    river2 = "River X"
    town2 = "My Town"
    s2 = MonitoringStation(s2_id, m2_id, label2, coord2, trange2, river2, town2)

    # Create a station
    s3_id = "test-s3-id"
    m3_id = "test-m3-id"
    label3 = "some station"
    coord3 = (-2.0, 4.0)
    trange3 = None
    river3 = "River X"
    town3 = "My Town"
    s3 = MonitoringStation(s3_id, m3_id, label3, coord3, trange3, river3, town3)

    assert s1.typical_range_consistent() is True
    assert s2.typical_range_consistent() is False
    assert s3.typical_range_consistent() is False


def test_inconsistent_typical_range_station():
    """Test of the inconsistent_typical_range_station function by
    creating a list of stations, using the tested function, and ensuring that
    any stations with inconsistent data is in the output of that function.
    """
    stations = build_station_list()  # Create a list of stations
    testoutput = inconsistent_typical_range_stations(stations)  # Use the tested function
    for i in stations:  # Iterate through the list of stations
        if i.typical_range_consistent() is False:
            assert i in testoutput  # If the station has inconsistent data, ensure that it
            # is in the test output

# --------------------------------------------------------------------------------
# Exercise 2B test


def test_relative_water_level():
    """Test of relative water level function to ensure it returns a correct value
    for relative water level and does not provide output when there is no data"""

    # Create a test station with level data
    s1_id = "test-s1-id"
    m1_id = "test-m1-id"
    label1 = "some station"
    coord1 = (-2.0, 4.0)
    trange1 = (-1.0, 3.0)
    river1 = "River X"
    town1 = "My Town"
    s1 = MonitoringStation(s1_id, m1_id, label1, coord1, trange1, river1, town1)
    s1.latest_level = 1.0

    # Create station without level data
    s2_id = "test-s2-id"
    m2_id = "test-m2-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (2.3, 3.4445)
    river2 = "River X"
    town2 = "My Town"
    s2 = MonitoringStation(s2_id, m2_id, label2, coord2, trange2, river2, town2)

    print("Output:\n{}\n{}".format(s1.relative_water_level(), s2.relative_water_level()))
    assert s1.relative_water_level() == 0.5     # assert if ratio is correct
    assert s2.relative_water_level() is None    # assert function has no output
# --------------------------------------------------------------------------------
