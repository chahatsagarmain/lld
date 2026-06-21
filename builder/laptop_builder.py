from laptop import Laptop

class LaptopBuilder:

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._laptop = Laptop()

    def set_cpu(self, cpu: str) -> "LaptopBuilder":
        self._laptop.cpu = cpu
        return self
    
    def set_gpu(self, gpu: str) -> "LaptopBuilder":
        self._laptop.gpu = gpu
        return self

    def set_ram_type(self, ram_type: str) -> "LaptopBuilder":
        self._laptop.ram_type = ram_type
        return self

    def set_ram_size(self, ram_size: str) -> "LaptopBuilder":
        self._laptop.ram_size = ram_size
        return self

    def set_screen_size(self, screen_size: str) -> "LaptopBuilder":
        self._laptop.screen_size = screen_size
        return self

    def build(self) -> Laptop:
        product = self._laptop
        self.reset()
        return product

