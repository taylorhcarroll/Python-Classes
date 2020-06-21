import datetime


class Building:
    def __init__(self, building_name, address, stories):
        self.building_name = building_name
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name

    def report(self):
        print(
            f'{self.building_name} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')
        print()


# Create 5 building instances
shakeys = Building("Shakeys Pizza", "800 8th Street", 8)
barbecutie = Building("Barbecutie", "900 9th Street", 11)
my_Home = Building("My Home", "1000 10th Street", 10)
test_building = Building("Test Building", "700 7th Street", 7)

# Have each one get purchased by a real estate magnate
shakeys.purchase("Jimothy Tabernacle")
barbecutie.purchase("Calico Caribou")
my_Home.purchase("Taylor Catroll")
test_building.purchase("Testing Testerman")


# After purchased, construct each one
shakeys.construct()
barbecutie.construct()
my_Home.construct()
test_building.construct()

shakeys.report()
barbecutie.report()
my_Home.report()
test_building.report()
