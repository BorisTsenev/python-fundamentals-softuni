class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circum = self.diameter * self.__pi
        return circum

    def calculate_area(self):
        radius = self.diameter / 2
        area = self.__pi * radius ** 2
        return area

    def calculate_area_of_sector(self, angle):
        area = (self.diameter / 2) ** 2 * self.__pi
        proportion = angle / 360
        sector_area = area * proportion
        return sector_area
