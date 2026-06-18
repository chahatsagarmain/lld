import threading
from tower import Tower
from phone_receiver import PhoneReceiver
from tv_receiver import TvReceiver

def start(tower: Tower, max_val: int) -> None:
    for _ in range(max_val):
        # Updating the signal automatically notifies all registered observers
        tower.update_signal()

if __name__ == "__main__":
    tower = Tower()
    tower.add_observer(PhoneReceiver())
    tower.add_observer(TvReceiver())
    
    t1 = threading.Thread(target=start, args=(tower, 5))
    t1.start()
    print("Started")
    t1.join()