# VSD_CNN_accelerator
## System architecture 
### NN architecture
![image](https://user-images.githubusercontent.com/73687292/215975748-bb8dd4ac-005a-44fb-8dd3-50be8a2da96d.png)
* Dataset
  * Source : Fruit Classification (kaggle)
  * Number of classes: 20 (fruits and vegetables)
  * Train : 200 img/per fruit, $Total = 200 * 20 = 4000 imgs$
  * Test : Average 50 img/per fruit, $Total = 50 * 20 = 100 imgs$
  * Image size: $32*32$
* Clip-Q 
  * So as to save the space of Mem
![image](https://user-images.githubusercontent.com/73687292/215975842-5890e854-0275-42aa-908f-9d4ffa3e3b06.png)
* Final Accuracy = $80.6％$

### HW architecture
![image](https://user-images.githubusercontent.com/73687292/215976256-43796d00-636b-4c18-8d64-be46b4838975.png)

### EPU architecture
* EPU structure
  * Weight  buffer(180KB)
  * Bias buffer(2KB)
  * Input buffer(384KB)
  * Output buffer(384KB)
* EPU mode
  * Conv3x3
  * 4PE,each with 9 MACs
  * zero padding
  * Relu
  * Conv1x1
  * 1PE with 9 MACs
  * Relu
  * Max pooling
![image](https://user-images.githubusercontent.com/73687292/215976317-cc004f6d-b4e7-43d0-ba0b-77e6a2cb5e93.png)

## Verification
### EPU Verify
1. Stand-alone testbench for EPU
2. TB loads input/weight/bias data into RTL-simulated SRAM buffers.
3. TB pulls start signal to high
4. EPU starts computation and writes results to output buffer.
5. EPU pulls finish signal to high
6. TB verify the content of output buffer.
### FULL Sys Verify
1. Assume ALL input/weight/bias data in DRAM.
2. CPU runs booting program with DMA.
3. Use DMA to move data from DRAM to EPU’s buffer.
4. CPU writes to EPU ctrl registers.
5. 8-bit weight shared by that layer “start” signal
6. EPU writes to output buffer as CPU stuck at WFI.
7. EPU finishes and send interrupt. CPU continues with ISR.
8. CPU writes ctrl signals for next layer.
9. Trigger “In-Output buffer swap”
10. Output of this layer is the input of next layer
11. If done, DMA move data from EPU to DRAM.
12. TB verify the content of DRAM.

## Overall Result
![image](https://user-images.githubusercontent.com/73687292/215977073-bfa4dc26-1d91-4d38-969c-d49c1be4c398.png)
![image](https://user-images.githubusercontent.com/73687292/215977134-2606d8be-ff7d-4a4d-a041-99c7861250cb.png)
![image](https://user-images.githubusercontent.com/73687292/215977163-b026cf41-195e-485e-a33e-001c8376369f.png)

## Contribution
* This project is complete with 黃昱澄 黃冠予 俞杉麒 陳奕萍 賴致文



