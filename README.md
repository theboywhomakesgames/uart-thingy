# uart-thingy
A Verilog uart simulation (kinda)


In this project, there is a python file that get's user input, sends the input to the iverilog through a hex file with only 9 bits in a serial way. Kinda like a uart port but not really. 


I coded this to help me communicate with my verilog code that I run using iverilog. That's the sole purpose of this project and it's really easy and minimal.


Be aware that there are bugs in converting the strings received back from the verilog code. It currently works for small cased characters only.
