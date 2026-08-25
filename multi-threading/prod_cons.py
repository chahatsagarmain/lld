from threading import Condition, Thread
from collections import deque

# Using deque for O(1) pops from the left side
q = deque()
max_len = 5
max_num = 10
cv = Condition()

def produce_item():
    # A for loop is much cleaner when you have a known number of iterations
    for num in range(max_num):
        with cv:
            while len(q) >= max_len:
                cv.wait()

            q.append(num)
            print(f"producer produced value {num}")
            cv.notify()
            
    # Send the poison pill AFTER the loop finishes producing normal items
    with cv:
        while len(q) >= max_len:
            cv.wait()
        q.append(-1)
        print("producer ended")
        cv.notify()

def consume_item():
    while True:
        with cv:
            while len(q) == 0:
                cv.wait()

            # popleft() is extremely fast compared to pop(0)
            val = q.popleft()
            print(f"consumer popped value {val}")
            
            if val == -1:
                print("consumer ended")
                break
                
            cv.notify()

def main():
    t1 = Thread(target=produce_item)
    t2 = Thread(target=consume_item)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()