"""Unit test for flood module"""
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

# --------------------------------------------------------------------------------
# EXERCISE 2B test


def test_stations_level_over_threshold():
    """Test for stations_level_over_threshold function to check it outputs correct
    data format (list of tuples) and sorts them properly"""

    # Create a working station
    s1_id = "test-s1-id"
    m1_id = "test-m1-id"
    label1 = "station 1"
    coord1 = (-2.0, 4.0)
    trange1 = (1.0, 2.0)
    river1 = "River X"
    town1 = "My Town"
    s1 = MonitoringStation(s1_id, m1_id, label1, coord1, trange1, river1, town1)
    s1.latest_level = 1.7

    # Create another working station with a higher relative level (should be sorted in front of 1)
    s2_id = "test-s2-id"
    m2_id = "test-m2-id"
    label2 = "station 2"
    coord2 = (-2.0, 4.0)
    trange2 = (2.0, 4.0)
    river2 = "River X"
    town2 = "My Town"
    s2 = MonitoringStation(s2_id, m2_id, label2, coord2, trange2, river2, town2)
    s2.latest_level = 3.6

    # Create a station out of 0.5 tol bounds
    s3_id = "test-s3-id"
    m3_id = "test-m3-id"
    label3 = "station 3"
    coord3 = (-2.0, 4.0)
    trange3 = (3.0, 6.0)
    river3 = "River X"
    town3 = "My Town"
    s3 = MonitoringStation(s3_id, m3_id, label3, coord3, trange3, river3, town3)
    s3.latest_level = 3.1

    stationlist = [s1, s2, s3]
    output = stations_level_over_threshold(stationlist, 0.5)

    print(output)
    assert len(output) == 2     # check last value is dropped
    assert output[0] == (s2.name, s2.relative_water_level())  # checks data form and order
    assert output[1] == (s1.name, s1.relative_water_level())

# --------------------------------------------------------------------------------
