import sys
from vehicle import Vehicle, VehicleBuilder
from ticket import Ticket, TicketManager
from parkinglot import ParkingLotManager, ParkingSlot

def print_separator(title: str):
    print(f"\n{'=' * 15} {title} {'=' * 15}")

def main():
    print_separator("INITIALIZING PARKING LOT")
    
    # Initialize ParkingLotManager and TicketManager
    parking_lot = ParkingLotManager()
    ticket_manager = TicketManager()
    
    # Add parking slots of different sizes
    # "LOW" represents small size, "MEDIUM" represents medium size, "HIGH" represents large size
    print("Adding parking slots...")
    parking_lot.add_parking_slot("LOW")       # Slot 1
    parking_lot.add_parking_slot("LOW")       # Slot 2
    parking_lot.add_parking_slot("MEDIUM")    # Slot 3
    parking_lot.add_parking_slot("MEDIUM")    # Slot 4
    parking_lot.add_parking_slot("HIGH")      # Slot 5
    
    print(f"Total slots: {parking_lot.num_slots}")
    print(f"Available slots initially: {parking_lot.available_slots}")
    for slot in parking_lot.get_parking_slots():
        print(f"  - {slot}")

    print_separator("CREATING VEHICLES")
    # Define some vehicles
    v1 = VehicleBuilder().add_vehicle_name("Honda Activa").add_vehicle_num(1024).add_vehicle_type("LOW").get_vehicle()
    v2 = VehicleBuilder().add_vehicle_name("Tesla Model 3").add_vehicle_num(2048).add_vehicle_type("MEDIUM").get_vehicle()
    v3 = VehicleBuilder().add_vehicle_name("Volvo Bus").add_vehicle_num(3096).add_vehicle_type("HIGH").get_vehicle()
    v4 = VehicleBuilder().add_vehicle_name("Toyota Prius").add_vehicle_num(4096).add_vehicle_type("MEDIUM").get_vehicle()
    v5 = VehicleBuilder().add_vehicle_name("Ducati Monster").add_vehicle_num(5012).add_vehicle_type("LOW").get_vehicle()

    vehicles = [v1, v2, v3, v4, v5]
    for vehicle in vehicles:
        print(f"Created vehicle: {vehicle}")

    print_separator("SIMULATING VEHICLE ARRIVALS (PARKING)")
    
    # We will park vehicles: Honda Activa (v1), Tesla Model 3 (v2), Volvo Bus (v3), Toyota Prius (v4)
    # Let's keep track of slot assignments for each vehicle
    active_parkings = {} # ticket_id -> slot_id
    
    for vehicle in [v1, v2, v3, v4]:
        print(f"\nAttempting to park vehicle: {vehicle.vehicle_name} ({vehicle.vehicle_type})...")
        
        # 1. Generate new ticket
        ticket_id = ticket_manager.get_new_ticket(vehicle)
        ticket = ticket_manager.get_ticket(ticket_id)
        print(f"  Generated {ticket}")
        
        # 2. Assign ticket to a slot
        try:
            slot_id = parking_lot.assign_ticket_to_slot(vehicle.vehicle_type, ticket)
            if slot_id is not None:
                active_parkings[ticket_id] = slot_id
            else:
                print(f"  Failed to park: No matching slot found for size {vehicle.vehicle_type}")
        except TypeError as e:
            print(f"  Failed to park: {e}")

    print_separator("CURRENT STATUS: SLOTS & TICKETS")
    print(f"Available slots count: {parking_lot.available_slots}")
    print("Available Slots list:")
    for slot in parking_lot.get_available_slots():
        print(f"  - {slot}")
        
    print("\nVehicles and their current parking status:")
    vehicle_statuses = parking_lot.get_parked_vehicles_status()
    for vehicle_name, status in vehicle_statuses.items():
        print(f"  - {vehicle_name}: {status}")

    print("\nAll Tickets History:")
    for ticket in ticket_manager.get_all_tickets():
        print(f"  - {ticket}")

    print_separator("SIMULATING PARKING OVERFLOW (DUCATI)")
    # Let's try to park Ducati (LOW).
    # Currently, 4 vehicles parked:
    #   - Slot 1 (LOW): Honda Activa
    #   - Slot 2 (LOW): AVAILABLE (wait, we parked Honda Activa, Tesla, Volvo, Prius)
    #   Wait, Honda Activa (LOW) goes to Slot 1 (LOW)
    #   Tesla Model 3 (MEDIUM) goes to Slot 3 (MEDIUM)
    #   Volvo Bus (HIGH) goes to Slot 5 (HIGH)
    #   Toyota Prius (MEDIUM) goes to Slot 4 (MEDIUM)
    # So Slot 2 (LOW) is still available.
    # If we park Ducati Monster (LOW), it should get Slot 2 (LOW).
    print(f"Attempting to park {v5.vehicle_name} ({v5.vehicle_type})...")
    t5_id = ticket_manager.get_new_ticket(v5)
    t5 = ticket_manager.get_ticket(t5_id)
    slot5_id = parking_lot.assign_ticket_to_slot(v5.vehicle_type, t5)
    if slot5_id is not None:
        active_parkings[t5_id] = slot5_id

    # Now all slots are occupied. Let's try to park another vehicle.
    v6 = VehicleBuilder().add_vehicle_name("Yamaha R1").add_vehicle_num(6099).add_vehicle_type("LOW").get_vehicle()
    print(f"\nAttempting to park {v6.vehicle_name} when lot is full...")
    t6_id = ticket_manager.get_new_ticket(v6)
    t6 = ticket_manager.get_ticket(t6_id)
    try:
        slot6_id = parking_lot.assign_ticket_to_slot(v6.vehicle_type, t6)
    except TypeError as e:
        print(f"  Error caught as expected: {e}")

    print_separator("SIMULATING DEPARTURE (PAYMENT & EXIT)")
    
    # 1. Honda Activa (v1) leaves. Let's find its ticket.
    # Active parkings has mapping: ticket_id -> slot_id.
    # Honda Activa has ticket_id = 1 (assigned to Slot 1).
    honda_ticket_id = 1
    honda_slot_id = active_parkings[honda_ticket_id]
    print(f"Honda Activa is ready to leave. Attempting to release Slot {honda_slot_id} without paying...")
    released = parking_lot.release_slot(honda_slot_id)
    print(f"  Slot released status: {released} (Expected: False, since ticket is unpaid)")
    
    # Now pay the ticket
    print("Paying ticket for Honda Activa...")
    paid = ticket_manager.pay_ticket(honda_ticket_id)
    print(f"  Payment successful: {paid}")
    
    # Try releasing slot again
    print("Releasing slot after payment...")
    released = parking_lot.release_slot(honda_slot_id)
    print(f"  Slot released status: {released} (Expected: True)")
    if released:
        active_parkings.pop(honda_ticket_id)

    # 2. Volvo Bus (v3) ticket_id = 3 (assigned to Slot 5).
    volvo_ticket_id = 3
    volvo_slot_id = active_parkings[volvo_ticket_id]
    print(f"\nPaying and releasing Volvo Bus (Slot {volvo_slot_id})...")
    ticket_manager.pay_ticket(volvo_ticket_id)
    released = parking_lot.release_slot(volvo_slot_id)
    print(f"  Slot released status: {released}")
    if released:
        active_parkings.pop(volvo_ticket_id)

    print_separator("FINAL PARKING LOT STATUS")
    print(f"Available slots count: {parking_lot.available_slots}")
    print("Available Slots list:")
    for slot in parking_lot.get_available_slots():
        print(f"  - {slot}")
        
    print("\nVehicles and their current parking status:")
    vehicle_statuses = parking_lot.get_parked_vehicles_status()
    if not vehicle_statuses:
        print("  - No vehicles currently parked.")
    for vehicle_name, status in vehicle_statuses.items():
        print(f"  - {vehicle_name}: {status}")

    print("\nAll Tickets History:")
    for ticket in ticket_manager.get_all_tickets():
        print(f"  - {ticket}")

if __name__ == "__main__":
    main()