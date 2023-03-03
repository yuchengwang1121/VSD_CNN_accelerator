
## Program flow
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

## How To Use
* Take conv0 for example
