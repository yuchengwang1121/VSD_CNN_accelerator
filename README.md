# VSD_CNN_accelerator

## Dataset
* Train : 200 img/per fruit, $Total = 200 * 33 = 6600 imgs$
* Test : Average 50 img/per fruit, $Total = 50 * 33 = 1650 imgs$

## Call
```python
python3 main.py --write # write In8, Bias32, Out8
main.py  --write --pretrained ./NIN/nin_p.pth.tar --evaluate
```
