class BMW:
    def __int__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("starting the car")

    def stop(self):
        print("stopping the car")


class ThreeSeries(BMW):
    def __int__(self, cruiseControlEnabled, make, model, year):
        super().__int__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print('Button Start')


class FiveSeries(BMW):
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__int__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled


threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
# threeSeries = ThreeSeries()
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
