from vehicle import Vehicle
from typing import Dict , List

class Ticket():

    def __init__(self , ticket_id : str , vehicle : Vehicle):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.ticket_status = "UNPAID"

    def pay_ticket(self):
        self.ticket_status = "PAID"

    def get_details(self) -> Dict[str , str]:
        return {
            "ticket_id" : str(self.ticket_id),
            "vehicle" : str(self.vehicle.vehicle_name),
            "ticket_status" : self.ticket_status
        }

    def __str__(self) -> str:
        return f"Ticket(ID: {self.ticket_id}, Vehicle: {self.vehicle.vehicle_name}, Status: {self.ticket_status})"

    def __repr__(self) -> str:
        return self.__str__()
    
class TicketManager():
    def __init__(self):
        self.tickets : Dict[int , Ticket] = {}
        self.tickets_count = 0
        self.unpaid_tickets = 0
        self.ticket_id = 0
        self.is_active = True

    def get_ticket(self , ticket_id : int) -> Ticket | None:
        return self.tickets.get(ticket_id , None)

    def get_new_ticket(self , vehicle : Vehicle) -> int:
        self.ticket_id += 1
        ticket = Ticket(
            ticket_id=str(self.ticket_id),
            vehicle=vehicle)
        self.tickets[self.ticket_id] = ticket
        self.tickets_count += 1
        self.unpaid_tickets += 1
        return self.ticket_id

    def pay_ticket(self , ticket_id : int) -> bool:
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            return False
        if ticket.ticket_status == "PAID": 
            return False
        ticket.pay_ticket()
        self.unpaid_tickets -= 1
        return True

    def remove_ticket(self , ticket_id : int):
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            return
        if ticket.ticket_status == "UNPAID":
            self.unpaid_tickets -= 1
        self.tickets.pop(ticket_id)
        self.tickets_count -= 1

    def get_all_tickets(self) -> List[Ticket]:
        tickets = []
        for itr in self.tickets.values():
            tickets.append(itr)
        return tickets




