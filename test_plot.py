"""Unit test for the plot submodule"""

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime


def test_plot_water_levels():
    """Test plot_water_levels function by giving it an input and
    ensuring the output is non-zero
    """
    stations = build_station_list()  # Create a list of stations
    update_water_levels(stations)  # Update the water levels
    station = stations[42]  # Take some station from that list
    dt = 5
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))  # Find dates and
    # waterlevels for that station

    output = plot_water_levels(station, dates, levels)  # Use tested function to get output

    assert output != 0  # Unsure what type this output would be (NoneType), but
    # should be non-zero


def test_plot_water_levels_with_fit():
    """Test plot_water_levels_with_fit by giving it an input and
    ensuring the output is non-zero
    """
    p = 3
    stations = build_station_list()  # Create a list of stations
    update_water_levels(stations)  # Update the water levels
    station = stations[42]  # Take some station from that list
    dt = 5
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))  # Find dates and
    # waterlevels for that station

    output = plot_water_level_with_fit(station, dates, levels, p)  # Use tested function to get output

    assert output != 0  # Unsure what type this plotted output would be (NoneType), but
    # should be non-zero
