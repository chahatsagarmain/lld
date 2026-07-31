from abc import ABC , abstractmethod

class Vehicle:

    def __init__(self , vehicle_name : str = None , vehicle_num : int = None , vehicle_type : str = None):
        self.vehicle_name = vehicle_name 
        self.vehicle_num = vehicle_num
        self.vehicle_type = vehicle_type

    def __str__(self) -> str:
        return f"Vehicle({self.vehicle_name}, Num: {self.vehicle_num}, Type: {self.vehicle_type})"

    def __repr__(self) -> str:
        return self.__str__()
    
class VehicleBuilder():

    def __init__(self):
        self.vehicle = Vehicle()

    def add_vehicle_name(self , vehicle_name : str) -> "VehicleBuilder":
        self.vehicle.vehicle_name = vehicle_name
        return self

    def add_vehicle_type(self , vehicle_type : str) -> "VehicleBuilder":
        self.vehicle.vehicle_type = vehicle_type
        return self

    def add_vehicle_num(self , vehicle_num : int) -> "VehicleBuilder":
        self.vehicle.vehicle_num = vehicle_num
        return self

    def get_vehicle(self) -> Vehicle:
        return self.vehicle