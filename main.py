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


def initialize_memory_bus(cpu):
    data_input = read_strip_data(DATA_INPUT_FILE)
    for data in data_input:
        data_parsed = data.split(",")
        address, value = data_parsed[0], data_parsed[1]
        cpu.write_memory_bus(address, value)


def send_cpu_instructions(cpu):
    instructions_input = read_strip_data(INSTRUCTION_INPUT_FILE)
    for instruction in instructions_input:
        cpu.parse_instructions(instruction)


# Run CPU Simulator
print("------------------------")
print("      CPU Simulator     ")
print("------------------------")

print("\nInstantiating CPU...")
cpu = CPU()

print("\nInitializing memory bus...")
initialize_memory_bus(cpu)

print("\nSending instructions to CPU...\n")

print("CPU Counter:" + str(cpu.get_cpu_counter_value()))
cpu.parse_instructions("JMP, 4")
print("CPU Counter: " + str(cpu.get_cpu_counter_value()))

send_cpu_instructions(cpu)