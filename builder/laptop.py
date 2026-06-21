class Laptop:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram_type = None
        self.ram_size = None
        self.screen_size = None

    def __str__(self):
        specs = [
            f"CPU: {self.cpu}" if self.cpu else None,
            f"GPU: {self.gpu}" if self.gpu else None,
            f"RAM Type: {self.ram_type}" if self.ram_type else None,
            f"RAM Size: {self.ram_size}" if self.ram_size else None,
            f"Screen Size: {self.screen_size}" if self.screen_size else None,
        ]
        return "Laptop Specifications:\n" + "\n".join(f" - {spec}" for spec in specs if spec)