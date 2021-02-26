from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Demonstration Program for Task 1C"""
    stations = build_station_list()  # Create list of station data
    centre = (52.2053, 0.1218)  # Set centre as Cambridge city centre
    r = 10  # radius of 10 km
    unsortedlist = []  # Initialise unsorted list
    stationsinradius = stations_within_radius(stations, centre, r)
    # Use demonstrated function
    for i in range(len(stationsinradius)):  # Iterate though list of stations
        stationname = stationsinradius[i].name
        # Take the name of the station from the list
        unsortedlist.append(stationname)
        # Add the name of the station to an unsorted list

    print(sorted(unsortedlist))
    # sort the list (should just be a list of strings) and print this


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
