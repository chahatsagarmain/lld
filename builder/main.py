from laptop_builder import LaptopBuilder

# The Builder Pattern is a Creational Design Pattern.
#
# Use case:
#   When you need to construct a complex object with many optional fields/parameters.
#   Instead of a bloated constructor with numerous positional or keyword arguments 
#   (which can lead to unreadable code and parameter ordering bugs), the Builder pattern 
#   provides a step-by-step construction process.
#
# Key Features:
#   - Decouples the representation and the construction process.
#   - Supports method chaining (each setter returns the builder instance).
#   - Provides a final 'build()' method to retrieve the completed product.

if __name__ == "__main__":
    print("--- Creating a Gaming Laptop via Builder Pattern ---")
    # Method chaining is now supported because setter methods return the builder instance.
    gaming_laptop = (
        LaptopBuilder()
        .set_cpu("Intel Core i7")
        .set_gpu("NVIDIA RTX 4070")
        .set_ram_type("DDR5")
        .set_ram_size("32GB")
        .set_screen_size("15.6 inch")
        .build()
    )
    print(gaming_laptop)
    print()

    print("--- Creating a Budget/Office Laptop with fewer custom specs ---")
    # Only setting the CPU and RAM, leaving other fields with default (None/unset) values.
    budget_laptop = (
        LaptopBuilder()
        .set_cpu("Intel Core i3")
        .set_ram_size("8GB")
        .build()
    )
    print(budget_laptop)