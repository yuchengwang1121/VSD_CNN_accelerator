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
## Verify each layer of NIN
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
Modify the `main.c`'s W8 with the W8 from H_data
```c
// Load W8 into EPU
  unsigned int w8 = 0x05FAED00;   //Modify this
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;
```
### 4. 
Create new file `parameter.hex` by self
```
00000020  //
00000003  //input channel
0000003C  //output channel
00000003  //
```
### 5.
```bash
# for verify Conv0 for example
cd ../..
make conv0
```

## Verify entire NIN
### 1. 
```bash
cd sim/conv_all
```
### 2.
Copy all layers's `bias.dat` `W2.dat` `parameter.dat` into conv_all 

### 3. 
Copy `in8_conv0.dat` from conv0 & `out8.hex` from pooling into conv_all 

### 4.
Modify main.c with each layer W8 from H_data
```c
/* conv0 */
  // Load W8 into EPU
  w8 = 0x05FAED00;
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;

/* conv1 */
  // Load W8 into EPU
  w8 = 0x07FBED00;
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;
  
/* conv2 */
  // Load W8 into EPU
  w8 = 0x06FBE600;
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;
```
### 5. 
```bash
# for verify Conv0 for example
cd ../..
make conv_all
```
