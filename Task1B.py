from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Demonstration Program for Task 1B"""

    stations = build_station_list()  # bring in data from stationdata
    p = (52.2053, 0.1218)  # set coordinates for Cambridge City Centre
    stationstownlist = []  # initialise empty output list
    stationslist = stations_by_distance(stations, p)
    # use function to be demonstrated
    closestfarthest = []
    # initialise empty list for closest/farthest 10 stations
    closestfarthest.extend(stationslist[:10])
    # add closest 10 stations to list
    closestfarthest.extend(stationslist[-10:])
    # add farthest 10 stations to list
    # print (len(stationslist))
    # ^used to test results - should be large
    # print (len(closestfarthest))
    # ^used to test results - should be 20 (10 times 2)
    for i in range(len(closestfarthest)):
        # set up iteration to find towns for the stations
        outputtuple = (closestfarthest[i][0].name, closestfarthest[i][0].town,
                       closestfarthest[i][1])
        stationstownlist.append(outputtuple)

    print(stationstownlist)  # print the output list


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
