class City:
    def __init__(self, name, mayor, date):
        self.name = name
        self.mayor = mayor
        self.year_established = date
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)
