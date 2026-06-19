# =====================================================================
# Singleton Design Pattern Example (Logger)
# =====================================================================
# Singleton is a creational design pattern that ensures a class has
# only a single instance in memory, providing a global point of access.
#
# Benefits:
# - Saves memory by reusing a single object.
# - Ensures consistent state across the codebase.
# - Coordinates access to shared resources (like log files or DB connections).
#
# Python Object Lifecycle:
# 1. __new__(cls, ...) allocates memory for the object and returns it.
# 2. __init__(self, ...) initializes the object's attributes.
#
# Crucial Singleton Detail:
# In Python, __init__ is called *every* time the class is invoked,
# even if __new__ returns a cached instance. To prevent resetting
# or overriding attributes on subsequent calls, we must use an 
# initialization guard.
# =====================================================================

import threading

class Logger:
    # Class-level variables to hold the single instance and a thread lock
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        # Implement double-checked locking for thread safety
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    # Allocate memory and create the single instance
                    cls._instance = super().__new__(cls)
        return cls._instance
        
    def __init__(self, file_name=None):
        # Bug Fix: Checked if the instance has NOT been initialized yet.
        # This guard prevents subsequent calls from resetting attributes.
        if not hasattr(self, "_initialized"):
            self.file_name = file_name
            self._initialized = True  # Set flag to true to skip future initializations

    def print_log(self, log: str):
        prefix = f"[{self.file_name}] " if self.file_name else ""
        print(f"{prefix}printing log : {log}")


# --- Demonstration and Verification ---
if __name__ == "__main__":
    # 1. Initialize the singleton logger with a file name
    log1 = Logger("app.log")
    
    # 2. Re-instantiate without parameters (or different parameters)
    log2 = Logger("override.log")  # Will not overwrite log1's file_name due to our initialization guard
    log3 = Logger()

    print("Verifying instance identities (should all be the same memory address):")
    print(f"log1 ID: {id(log1)} (File Name: {log1.file_name})")
    print(f"log2 ID: {id(log2)} (File Name: {log2.file_name})")
    print(f"log3 ID: {id(log3)} (File Name: {log3.file_name})")
    
    print("\nTesting printing capability:")
    log1.print_log("First log message.")
    log2.print_log("Second log message from another reference.")