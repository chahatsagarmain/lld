from typing import List , Dict
from ticket import Ticket , TicketManager

class ParkingSlot:

    def __init__(self , slot_id : int , slot_type : str):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.status = "AVAILABLE"
        self.ticket = None

    def assign_ticket(self , ticket : Ticket) -> None:
        self.ticket = ticket
        self.status = "OCCUPIED"

    def unassign_slot(self) -> None:
        self.ticket = None
        self.status = "AVAILABLE"

    def get_status(self) -> str:
        return self.status

    def get_ticket(self) -> Ticket:
        return self.ticket

    def __str__(self) -> str:
        return f"Slot(ID: {self.slot_id}, Type: {self.slot_type}, Status: {self.status})"

    def __repr__(self) -> str:
        return self.__str__()

class ParkingLotManager():

    def __init__(self):
        self.num_slots : int = 0
        self.parking_slots : Dict[int , ParkingSlot] = {}
        self.available_slots : int = 0
        self.slot_id : int = 0
        self.slot_vals = {
            "LOW" : 0,
            "MEDIUM" : 1,
            "HIGH"  : 2
        }

    def add_parking_slot(self , slot_type : str):
        if slot_type not in {"LOW" , "MEDIUM" , "HIGH"}:
            raise TypeError("Invalid Input")
        self.num_slots += 1
        self.available_slots += 1
        self.slot_id += 1
        self.parking_slots[self.slot_id] = ParkingSlot(
            slot_id=self.slot_id,
            slot_type=slot_type
        )

    def assign_ticket_to_slot(self , vehicle_type : str , ticket : Ticket) -> int | None:
        if self.available_slots == 0:
            raise TypeError("No slots available")

        found = False
        slot_id = -1
        diff = 100
        for slot in self.parking_slots.values():
            if slot.status != "AVAILABLE":
                continue
            if self.slot_vals[vehicle_type] == self.slot_vals[slot.slot_type]:
                found = True 
                slot_id = slot.slot_id
                break
            if self.slot_vals[slot.slot_type] > self.slot_vals[vehicle_type] and diff > self.slot_vals[slot.slot_type] - self.slot_vals[vehicle_type]:
                diff = self.slot_vals[slot.slot_type] - self.slot_vals[vehicle_type]
                found = True 
                slot_id = slot.slot_id

        if not found:
            print("No valid slot found for vehicle")
            return None

        self.parking_slots[slot_id].assign_ticket(ticket)
        self.available_slots -= 1
        print(f"ticket {ticket.ticket_id} assigned to slot {self.parking_slots[slot_id].slot_id}")
        return slot_id


    def release_slot(self , slot_id) -> bool:
        if self.parking_slots.get(slot_id , None) is None:
            print("INVALID SLOT ID")
            return False
        
        if self.parking_slots[slot_id].status == "AVAILABLE":
            return True

        if self.parking_slots[slot_id].ticket.ticket_status != "PAID":
            return False

        self.parking_slots[slot_id].unassign_slot()
        self.available_slots += 1

        return True


    def get_parking_slots(self) -> List[ParkingSlot]:
        slots = []
        for itr in self.parking_slots.values():
            slots.append(itr)
        return slots

    def get_available_slots(self) -> List[ParkingSlot]:
        return [slot for slot in self.parking_slots.values() if slot.status == "AVAILABLE"]

    def get_parked_vehicles_status(self) -> Dict[str, str]:
        status_dict = {}
        for slot in self.parking_slots.values():
            if slot.status == "OCCUPIED" and slot.ticket is not None:
                status_dict[slot.ticket.vehicle.vehicle_name] = f"Parked in Slot {slot.slot_id} (Ticket: {slot.ticket.ticket_status})"
        return status_dict
