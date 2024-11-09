from cpu import CPU

'''
CPU COMMAND KEY

INSTRUCTION
| Argument - Purpose

CACHE
| 0 - Turn cache off
| 1 - Turn cache on
| 2 - Flush cache

JMP
| # - Jump to specified position

'''

# Reference input files
DATA_INPUT_FILE = "Inputs/data_input.txt"
INSTRUCTION_INPUT_FILE = "Inputs/instruction_input.txt"


# Read data from file and strip whitespace
def read_strip_data(filepath):
    # Open file in read mode
    file = open(filepath, 'r')
    # Read lines from file
    data = file.readlines()
    # Strip whitespace using anonymous lambda function
    data = list(
        map(
            lambda s: s.strip(), data
        )
    )
    return data


data_input = read_strip_data(DATA_INPUT_FILE)
instructions_input = read_strip_data(INSTRUCTION_INPUT_FILE)

# Run CPU Simulator
print("------------------------")
print("      CPU Simulator     ")
print("------------------------")
print("")
print("Instantiating CPU...")
cpu = CPU()
print("\nSending instructions to CPU...")

cpu.parse_instructions("CACHE, 0")
cpu.parse_instructions("CACHE, 1")
cpu.parse_instructions("CACHE, 2")

print("CPU Counter:" + str(cpu.get_cpu_counter_value()))
cpu.parse_instructions("JMP, 1")
print("CPU Counter: " + str(cpu.get_cpu_counter_value()))
