from cache import Cache
from memory import Memory

# Instruction operators
ADD_INSTR_OPERATOR = "ADD"
ADD_I_INSTR_OPERATOR = "ADD1"
JUMP_INSTR_OPERATOR = "JMP"
CACHE_INSTR_OPERATOR = "CACHE"

# Cache status values
CACHE_OFF_VALUE = 0
CACHE_ON_VALUE = 1
CACHE_FLUSH_VALUE = 2

# Initialize CPU constants
CPU_COUNTER_INIT_VALUE = 0
NUM_REGISTERS = 9


class CPU:
    def __init__(self):
        self.memory_bus = Memory()
        self.cache = Cache()
        self.cache_flag = False
        self.cpu_counter = CPU_COUNTER_INIT_VALUE
        # Creates list NUM_REGISTERS long with [0, 0, ...]
        self.registers = [0] * NUM_REGISTERS

    # Memory bus methods
    def write_memory_bus(self, address, value):
        self.memory_bus.write_memory_bus(address, value)

    def search_memory_bus(self, address):
        self.memory_bus.search_memory_bus(address)

    # Cache methods
    def flush_cache(self):
        self.cache.flush_cache()

    def write_cache(self, address, value):
        self.cache.write_cache(address, value)

    def search_cache(self, address):
        self.cache.search_cache(address)

    # CPU counter methods
    def reset_cpu_counter(self):
        self.cpu_counter = CPU_COUNTER_INIT_VALUE

    def increment_cpu_counter(self):
        self.cpu_counter += 1

    def get_cpu_counter_value(self):
        return self.cpu_counter

    # Register methods
    def reset_registers(self):
        for i in range(len(self.registers)):
            self.registers[i] = 0
