# lets do print even odd but with a lock 

import threading

total_num = 100
num = 0

global_lock = threading.Lock()

def print_even():
    global num
    while True:
        with global_lock:
            if num > total_num:
                break
            if num % 2 == 0:
                print(f"even thread printing {num}")
                num += 1

def print_odd():
    global num
    while True:
        with global_lock:
            if num > total_num:
                break
            if num % 2 != 0:
                print(f"odd thread printing {num}")
                num += 1

def main():
    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()