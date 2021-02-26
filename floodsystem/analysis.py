"""This submodule contains functions for analysing the water level data
"""
# polyfit requirements
import numpy as np
import matplotlib

# risk_by_gradient requirements (needs polyfit and its requirements as well)
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def polyfit(dates, levels, p):
    """This function computes a least-squares fit of a polynomial of degree
    "p" (an integer), given the water level time history (dates(YYYY-MM-DD)
    and levels (floats)).
    """

    datesnum = matplotlib.dates.date2num(dates)  # Uses matplotlib date2num function to turn
    # list of dates into a float of days since the year 0001.
    p_coeff = np.polyfit(datesnum - datesnum[0], levels, p)  # Finds polynomial coefficients for
    # dates (subtracting the first date from each in order to have smaller numbers to work with),
    # as well as the list of levels corresponding to each date and the coefficient p
    poly = np.poly1d(p_coeff)  # Converts the coefficients into a polynomial that can be evaluated
    d0 = datesnum[0]  # Sets d0 as the date offset used before
    return (poly, d0)  # returns the polynomial function (type poly1d) and the offset (type float)

# Various Testing parts (commented out, IGNORE)
# ----------------------------------------------------------------------

# stations = build_station_list()
# dates, levels = fetch_measure_levels(station[1].measure_id, dt=datetime.timedelta(days=dt))
# poly, d0 = polyfit(dates, levels, p)
# plt.plot(dates, poly(dates-d0))
# plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# EXERCISE 2G - Calculating station risk by gradient


def risk_by_gradients(station, dt, p):
    """This function calculates flood risk for a station by producing a polynomial function order p over the past dt days,
    then comparing the 1st and 2nd derivatives against set conditions. Returns risk as string"""

    # STATION DATA TYPE CHECK
    if ((station.typical_range_consistent() is False) or (type(station.relative_water_level()) is not float)
            or type(station) is not MonitoringStation):     # checks data types
        raise TypeError("Invalid data type for station")

    # INPUT DATA TYPE CHECK
    if ((type(dt) is not int) or (type(p) is not int)):     # checks data types
        raise TypeError("Invalid data type, arguments dt and p must be integers")
    elif p < 2:     # checks value of p
        raise ValueError("P must be greater than 2")

    # FETCH DATES/LEVELS DATA FOR STATION
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    # dates/levels data checks
    if ((type(levels) is not list) or (type(dates) is not list)    # checks if data is list
        or (len(levels) == 0) or (len(dates) == 0)    # checks if there is data in arrays
            or len(levels) != len(dates)):   # checks if there is equal date and level data
        raise TypeError("Invalid data type for dates/levels")

    # CALCULATE POLYNOMIAL FUNCTION AND DERIVATIVES
    function, d0 = polyfit(dates, levels, p)    # create polynomial function
    deriv1 = function.deriv(1)      # calculate 1st derivative
    deriv2 = function.deriv(2)      # calculate 2nd derivative

    # CALCULATE CURRENT VALUE OF DERIVATIVES
    datesnum = matplotlib.dates.date2num(dates)     # convert dates to float
    x_current = datesnum[-1] - datesnum[0]   # sets value for current date

    d1val = 0   # initialise value for 1st derivative
    for power in range(len(deriv1)):    # iterate through coefficients
        d1val += (deriv1[power] * (x_current ** power))     # calculates respective entry

    d2val = 0   # initialise value for 2nd derivative
    for power in range(len(deriv2)):    # iterate through coefficients
        d2val += (deriv2[power] * (x_current ** power))     # calculates respective entry

    # EVALUATING RISK LEVEL
    risk = "-"  # sets up variable risk
    # if gradient positive/stable and increasing/stable -> high risk
    if ((d1val >= 0) and (d2val >= 0)):
        risk = "high risk"
    # if gradient positive/stable and decreasing -> moderate risk
    elif ((d1val >= 0) and (d2val < 0)):
        risk = "moderate risk"
    # if gradient negative and increasing/stable -> moderate risk
    elif ((d1val < 0) and (d2val >= 0)):
        risk = "moderate risk"
    # if gradient negative and decreasing -> low risk
    elif ((d1val < 0) and (d2val < 0)):
        risk = "low risk"
    # handles errors when above logic fails
    else:
        raise ValueError("Invalid function for {}".format(station.name))

    return(risk)   # returns output
# ----------------------------------------------------------------------------------------------------------------------
