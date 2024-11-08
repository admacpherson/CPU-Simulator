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