class vehicle:

    def __init__(self, name, wheels, engines, seats):
        self.name = name
        self.wheels = wheels
        self.engines = engines
        self.seats = seats

    def getDetails(self):
        print("The vehicle",self.name,"has wheels:",self.wheels,"has engines:",self.engines,"has seats:",self.seats)

    # def getProperties(self):
    #     print("The vehicle",self.name,"has wheels:",self.wheels,"has engines:",self.engines,"has seats:",self.seats)

class flyingVehicle(vehicle):
    def __init__(self, wingsCount, cocpitSeats):
        self.wingCount = wingsCount
        self.cocpitSeats = cocpitSeats

    def getDetails(self):
        print("this is a flying vehicle with wings:",self.wingsCount,"and cocpitSeats:",self.cocpitSeats)

fv = flyingVehicle(2,2)
fv.getDetails()

# class car(vehicle):
#     pass

# vehicle1 = vehicle("car",4,1,2)
# car1 = car("Mercedes benz",4,1,2)
# car1.getProperties()
#
# car2 = car("Ecosport",4,1,5)
# car2.getProperties()

