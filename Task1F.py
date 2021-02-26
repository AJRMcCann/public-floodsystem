from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    """Demonstration Program for Task 1F"""
    stations = build_station_list()  # Create list of station data
    unsortedlist = []  # Initialise unsorted list
    baddatastationlist = inconsistent_typical_range_stations(stations)
    # Create an (unsorted) list of stations
    # using the demonstrated function

    for station in baddatastationlist:
        # Iterate through list of stations with inconsistent data
        unsortedlist.append(station.name)
        # Add the station name to the unsorted list

    sortedlist = sorted(unsortedlist)  # Create an alphabetically sorted list
    if sortedlist is None:
        print("No Inconsistent Data in Stations List")
        # Print this message if there is no inconsistent data
    else:
        print(sortedlist)
        # Print the list of stations with inconsistent data if it exists


if __name__ == "__main__":  # Running the demonstration program
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
