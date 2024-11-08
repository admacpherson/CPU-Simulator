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
CPU_COUNTER_VALUE = 0
NUM_REGISTERS = 9

class CPU:
    def __init__(self):
        self.memory_bus = Memory()
        self.cache = Cache()
        self.cache_flag = False
        self.cpu_counter = CPU_COUNTER_VALUE
        # Creates list NUM_REGISTERS long with [0, 0, ...]
        self.registers = [0] * NUM_REGISTERS

    