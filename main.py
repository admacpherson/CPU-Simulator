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


