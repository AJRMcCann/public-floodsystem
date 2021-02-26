"""Unit test for the geo module"""
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_within_radius, plot_on_map


def test_stations_by_distance():  # Add test for stations_by_distance function
    """Test stations by distance function by checking length and validity of output"""
    stations = build_station_list()  # Create list of stations for testing
    p = (0, 0)  # p can be anything for the test
    output = stations_by_distance(stations, p)  # Use the tested function
    assert len(output) > 0  # Ensure that it outputs something
    assert output[0][1] > 0 or output[2][1] > 0  # Ensure that it outputs a non-zero distance
    # (or a non-zero distance for another tuple on the small chance that one station is exactly
    # at p)
    assert type(output[0][0]) == MonitoringStation  # Ensure that the type of object in the "station" section is
    # a MonitoringStation object
    assert type(output[0][1]) == float  # Ensure that the type of object in the "distance" section
    # is a float


def test_stations_within_radius():  # Add test for stations_within_radius function
    """Test stations_within_radius function by having it find all the stations within
    a large radius and ensuring the output is all of the stations"""
    stations = build_station_list()  # Create list of stations for testing
    centre = (53, -1)  # Put the centre (roughly) in the middle of the UK
    # (according to the data from DEFRA, the extent of the stations is between
    # Lat 49.9-55.8 and Long -6.2 - 2.1)
    r = 1500  # Set a large radius to guarantee encompassing all of the stations
    output = stations_within_radius(stations, centre, r)  # Use the test function

    if len(stations) == 0:  # Ensure that there is some data to be tested
        # from the source
        raise ValueError("Source list gives no data")
    else:
        assert len(output) > 0  # Ensure that it outputs some data
        assert type(output[0]) == MonitoringStation  # Ensure that it is outputting a list of names
        # in MonitoringStation format
        assert len(output) == len(stations)  # Make sure that it includes all of the stations
        # (as r and centre are set so that it should encompass all of the stations)


def test_plot_on_map():
    """Test plot_on_map function by ensuring it gives some output"""
    list_of_stations = build_station_list()  # Create list of stations to test from
    assert plot_on_map(list_of_stations) != 0  # Unsure what the output of this function will
    # look like, but should be non-zero (i.e. some output).
