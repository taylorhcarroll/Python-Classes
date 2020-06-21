import datetime
import building
from city import City

townsville = City("Townsville", "Mayor Mayorson",
                  datetime.datetime.now())
townsville.add_building(building.my_Home)
townsville.add_building(building.shakeys)
townsville.add_building(building.test_building)

for building in townsville.buildings:
    print(f"In the city of {townsville.name} {building.address} was purchased by a {building.owner} on {building.date_constructed} and has {building.stories} stories.")
