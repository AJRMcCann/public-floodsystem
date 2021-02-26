"""Unit test for the analysis submodule"""

import datetime
from floodsystem.analysis import polyfit, risk_by_gradients
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level


def test_polyfit():
    """Test of the polyfit function by
    """
    p = 5  # Arbitrary number for degree of polynomial
    stations = build_station_list()  # Build test list of stations
    station = stations[25]  # Take an arbitrary station from that list
    dt = 4  # Arbitrary number of days for testing
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))  # Set dates
    # and levels for tested station
    output = polyfit(dates, levels, p)  # Use tested function to create output
    assert type(output) is tuple  # Make sure the output of the tested function is a tuple
    assert type(output[1]) is float or int  # Make sure the d0 part of the tested function's output is a
    # float or integer


def test_risk_by_gradients():
    """Tests risk_by_gradients function"""

    stations = build_station_list()  # build station list
    update_water_levels(stations)   # update water levels
    topstation = stations_highest_rel_level(stations, 1)
    for i in stations:
        if i.name == topstation[0]:
            station = i
    testlist = risk_by_gradients(station, 7, 2)

    print(testlist)


test_risk_by_gradients()
