# File Structure
### include
* The define files to define specific len of data into string.
### script
* The setting files for APR and synthesis.
### sim
* Store files associated with .hex, .dat, setup and boot.c.
### src
* `AXI` : The AXI protocal implementation.
* `CPU` : The sub module for `CPU.sv`.
* `DMA` : The Direct Memory Access to move the data from DRAM into EPU.
* `EPU` : The added unit to calculate the network layers.
* `Interface` : The file to union the wire into interface.
* `Others` : See the HW4's Explanation
### syn
* The systhesis file after $Make synthesis$
### Make file
* To call $Make XXX$ to verify the correctly of the result

# How to use
* 
