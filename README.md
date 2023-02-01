# VSD_CNN_accelerator
## System architecture
### NN architecture
* NIN model structure
  * We use NIN to improve the accurancy of detection with less parameter needed,
  * model structure :
    ![image](https://user-images.githubusercontent.com/73687292/215978510-056a30d3-442a-4f86-b6e2-85c2a4a12e19.png)
* Dataset
  * Source : Fruit Classification (kaggle)
  * Number of classes: 20 (fruits and vegetables)
  * Train : 200 img/per fruit, $Total = 200 * 20 = 4000 imgs$
  * Test : Average 50 img/per fruit, $Total = 50 * 20 = 100 imgs$
  * Image size: $32*32$
* Clip-Q
  * Clip-Q is used to save the usage of Mem
  * Clip-Q Step :
  ![image](https://user-images.githubusercontent.com/73687292/215978048-e9390e57-0a71-429e-a343-7c77aa3f31b5.png)
  * Clip-Q example :
  ![image](https://user-images.githubusercontent.com/73687292/215978230-d5813d08-4d2b-4f5b-bf23-803b62f18b0e.png)
* Final Accuracy = 80.6%
### HW architecture
* The HW component's details 
  ![image](https://user-images.githubusercontent.com/73687292/215978622-be2a883c-f09f-442f-9dd5-745bf2328831.png)

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

![image](https://user-images.githubusercontent.com/73687292/215978699-00b778bf-ae91-4a1c-adde-a5153024926e.png)

## Verification
### EPU verification
1. Stand-alone testbench for EPU
2. TB loads input/weight/bias data into RTL-simulated SRAM buffers.
3. TB pulls start signal to high
4. EPU starts computation and writes results to output buffer.
5. EPU pulls finish signal to high
6. TB verify the content of output buffer.

### Full sys verification
1. Assume ALL input/weight/bias data in DRAM.
2. CPU runs booting program with DMA.
3. Use DMA to move data from DRAM to EPU’s buffer.
4. CPU writes to EPU ctrl registers.
5. 8-bit weight shared by that layer “start” signal.
6. EPU writes to output buffer as CPU stuck at WFI.
7. EPU finishes and send interrupt. CPU continues with ISR.
8. CPU writes ctrl signals for next layer.
9. Trigger “In-Output buffer swap”
10. Output of this layer is the input of next layer
11. If done, DMA move data from EPU to DRAM.
12. TB verify the content of DRAM.

## Overall results
![image](https://user-images.githubusercontent.com/73687292/215979233-0d3edcd1-fb30-4b23-be9f-d9c21f4955bc.png)
![image](https://user-images.githubusercontent.com/73687292/215979265-f0097f55-fd8e-40a2-85a4-ddde3f7108e1.png)
![image](https://user-images.githubusercontent.com/73687292/215979292-884c3d2c-d09c-453f-bbcd-5649acafc873.png)

## Contribution
Thanks to 黃昱澄 黃冠予 俞杉麒 陳奕萍 賴致文 to complete this project.
 
