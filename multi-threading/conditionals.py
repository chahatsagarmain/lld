
import threading

# conditional variables are one the crazeist way to syncrhonize threads 
# so conditional variabels need a lock 
# they work like normal locks but they expose wait and notify and notify_all method 

# wait means that this thread is sent to sleep state 
# the thead gives up lock and lets other thread acquire lock 

# notify , notify means that one of the waiting thread is notified to be ready for execution when lock is released 

# notify_all , all the waiting threads are notfied 


cv = threading.Condition()
mx = 100
num = 0

def print_even():
    global num
    while True:
        # acquire the lock to access the critical section
        with cv:
            while num % 2 and num <= mx:
                # if num is odd and <= mx, we send even thread to sleep
                # and release the lock for the odd thread
                cv.wait()
            if num > mx:
                break
            if num % 2 == 0:
                print(f"even thread printing {num}")
                num += 1
                # wake up the odd thread
                cv.notify()

def print_odd():
    global num
    while True:
        with cv:
            while num % 2 == 0 and num <= mx:
                cv.wait()
            if num > mx:
                break
            if num % 2 != 0:
                print(f"odd thread printing {num}")
                num += 1
                cv.notify()
def main():
    t1 = threading.Thread(target=print_even)
    t2 = threading.Thread(target=print_odd)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()

