
# when accessing critical resource there is a very big anomaly that can happen called as race condition 
# two threads running parallely trying to access a same resouce at the same time 
# to prevent this you use mutex or locks ( mutex as in mutual exclusion get it ? )
# so lets try this out , the main idea is when trying to read a shared resource only one thread should be allowed at once 

import threading
import time

num = 0

def race_condition_demo():
    mx = 1000000 
    
    def count_up():
        global num
        for _ in range(mx):
            num += 1 

    t1 = threading.Thread(target=count_up)
    t2 = threading.Thread(target=count_up)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def demo_with_lock():
    mx = 1000000 
    lock = threading.Lock() 
    
    def count_up():
        global num
        for _ in range(mx):
            with lock:
                num += 1
    
    t1 = threading.Thread(target=count_up)
    t2 = threading.Thread(target=count_up)
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def main():
    global num
    
    print("--- Running without locks ---")
    start_time = time.perf_counter()
    race_condition_demo()
    end_time = time.perf_counter()
    
    print(f"Final counter value: {num}")
    print(f"Time taken: {end_time - start_time:.4f} seconds\n")
    
    num = 0 # reset counter
    
    print("--- Running with locks ---")
    start_time = time.perf_counter()
    demo_with_lock()
    end_time = time.perf_counter()
    
    print(f"Final counter value: {num}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")

    # if you notice the lock version ,takes signficantlty more time 
    # why ? 
    # lock acquistion and release takes time simple 
    # the other thread waiting for lock , has to wait for the lock to be released


if __name__ == "__main__":
    main()