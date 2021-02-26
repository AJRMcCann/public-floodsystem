from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Task 1E"""
    stations = build_station_list()   # build list of stations
    N = 9     # define number of rivers to display
    riversbystat = rivers_by_station_number(stations, N)   # function from 1e
    print("\nTop {0} Rivers by Stations: \n {1}\n"
          .format(N, riversbystat))     # output


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
