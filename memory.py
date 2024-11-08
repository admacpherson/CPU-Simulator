# Memory bus size constant
MEMORY_BUS_SIZE = 28

# Creates a simulated memory bus as a dictionary
class Memory:
    def __init__(self):
        self.memory_bus = {}
        self.init_memory_bus()

    # Initialized memory bus parameter by initializing 0 through MEMORY_BUS_SIZE as 8-digit binary string
    def init_memory_bus(self):
        for i in range(MEMORY_BUS_SIZE):
            self.memory_bus['{0:08b}'.format(i)] = 0

    # Write a specified value to the memory bus at a specified address
    def write_memory_bus(self, address, value):
        # Check that address exists
        if self.memory_bus.get(address) is not None:
            self.memory_bus[address] = value

    # Search memory bus by address and return value
    def search_memory_bus(self, address):
        return self.memory_bus.get(address)