# CPU-Simulator
Python program to simulate CPU functionalities using OOP structure.

## Structure
📁[inputs](https://github.com/admacpherson/CPU-Simulator/tree/main/Inputs) - Modifiable input files to be read into simulation<br>
| [`data_input`](https://github.com/admacpherson/CPU-Simulator/blob/main/Inputs/data_input.txt) - Contains sample data that are read into memory bus<br>
| [`instruction input`](https://github.com/admacpherson/CPU-Simulator/blob/main/Inputs/instruction_input.txt) - Contains sample instructions that are read into CPU<br>

[`cache.py`](https://github.com/admacpherson/CPU-Simulator/blob/main/cache.py) - Cache class<br>
[`cpu.py`](https://github.com/admacpherson/CPU-Simulator/blob/main/cpu.py) - CPU class that contains the bulk of the applicable programming. Utilizes intstantiations of the cache and memory bus<br>
[`main.py`](https://github.com/admacpherson/CPU-Simulator/blob/main/main.py) - Instantiates CPU, reads applicable data, and runs the simulation<br>
[`memory.py`](https://github.com/admacpherson/CPU-Simulator/blob/main/memory.py) - Memory bus class

## Instruction Key
|Command|Argument|Function|
|---|---|---|
|CACHE|0|Turn cache off|
|CACHE|1|Turn cache on|
|CACHE|2|Flush cache|
|JMP|<i>INT</i>|Jump to specified position
|ADD|<i>Destination, Source, Target</i>|Add target and source register values on destination register|
|ADDI|<i>Destination, Source, Immediate</i>|Add immediate value to source register on destination register|
|HALT||Halt program|

## References
Code is based on <a href="https://codecadmy.com">Codecademy's</a> <a href="https://github.com/Codecademy/computer-architecture/tree/main/portfolio-project-cpu-simulator">CPU Simulator Portfolio Project</a>.<br>

Thanks to Dr. Timothy Heil for his computer architecture knowledge.
