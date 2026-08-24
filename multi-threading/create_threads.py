import threading

# in this file lets try create threads 

def func():
    print("func with no argument")

def func_with_arg(arg: int):
    print(f"func with an argument {arg}")

def main():
    # Create a thread to run the func function
    t1 = threading.Thread(target=func)
    # Start the thread
    t1.start()

    # Wait for its execution and join the main thread
    t1.join()

    # Create the thread with func_with_arg and pass 0 as a tuple argument
    t2 = threading.Thread(target=func_with_arg, args=(0,))
    t2.start()
    t2.join()

    # Let's try running multiple threads
    threads = []
    for i in range(1, 6):
        t = threading.Thread(target=func_with_arg, args=(i,))
        threads.append(t)
        t.start()

    # Wait for all spawned threads to complete
    for t in threads:
        t.join()
    

if __name__ == "__main__":
    main()


