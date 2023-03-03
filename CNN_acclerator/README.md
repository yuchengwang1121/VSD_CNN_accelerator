# Program flow
- Assume ALL input/weight/bias data in DRAM.
- CPU runs booting program with DMA.
- Use DMA to move data from DRAM to EPU’s buffer.
- CPU writes to EPU ctrl registers which starts up EPU.
- EPU writes to output buffer as CPU stuck at WFI.
- EPU finishes and send interrupt. CPU continues with ISR.
- CPU writes ctrl signals for next layer.
  - Trigger “In-Output buffer swap”
  - Output of this layer is the input of next layer
- If done, DMA move data from EPU to DRAM.
- TB verify the content of DRAM.

# How To Use
### Convolution : Take conv0 for example
1. Go into the file sim/conv0 and then copy `Bias32.hex`, `In8.hex`, `Out8.hex`, `W2.hex` into the file.
  ```shell
  cd sim/conv0
  // copy the *.hex files in here
  ```
2. Create the `parameter.hex`
  ```
  00000020    //Input size
  00000003    //Input channel
  0000003C    //Output channel
  00000003    //Output ????
  ```
3. Run the below command to generate *.hex into *.dat
  ```python
  ```
4. Modify the W8 with W8.hex in main.c
  ```c
  // Load W8 into EPU
  unsigned int w8 = 0x05FAED00;   //Modify this line
  *epu_w8_l_addr = w8;
  *epu_w8_u_addr = w8 >> 16;
  ```
5. Run the make command to verify the convolution layer
  ```makefile
  make conv0
  ```
### Maxpooling : Take  pool0 for example
1. Go into the file sim/pool0 and then copy `In8.hex`, `Out8.hex`into the file.
  ```shell
  cd sim/pool0
  // copy the *.hex files in here
  ```
2. Create the `parameter.hex`
  ```
  00000020    //Input size
  00000014    //Input channel
  00000014    //Output size
  00000020    //Output ????
  ```
3. Run the below command to generate *.hex into *.dat
  ```python
  ```
4. Run the make command to verify the convolution layer
  ```makefile
  make pool0
  ```
### Conv_all
  
