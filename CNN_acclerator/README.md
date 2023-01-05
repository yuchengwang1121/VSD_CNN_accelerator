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
* `Others` : See the [HW4's Explanation](https://github.com/yuchengwang1121/VLSI-System-Design/tree/main/HW4/DOC)
### syn
* The systhesis file after $Make synthesis$
### Make file
* To call $Make XXX$ to verify the correctly of the result

# How to use
### 1. 
```bash
# for verify Conv0 for example
cd sim/conv0
```
### 2. 
Copy the corrseponding `.hex` into the file then run below code to generate `.dat` & `.o` 
```python
python3 conv2bin.py
```
### 3.
Modify the `main.c`'s W8 with the W8 in H_data
```c
// Load W8 into EPU
  unsigned int w8 = 0x05FAED00;   //Modify this
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;
```
### 4.
```bash
# for verify Conv0 for example
cd ../..
make conv0
```
