# File Structure
### ClipQ
* `util.py` : The ClipQ implement.
* `util_write.py` : The ClipQ implement. And the weight files "W2, W8" is created.
* `Qfile.py` : Calculate the weight of the weight in kernal 1x1 & 3x3.
* `chQfile.py` : Calculate the W8 for EPU to load in main.c.
### H_data
* The hex data for EPU to transform into dat file
### NIN
* `nin.py` : The NIN network structure. And the in, out and bias files "IN8. Bias32, Out8" is created.
* `Qfile.py` : Calculate the bias in convolution layer.
* `chQfile.py` : Calculate the input and output in convolution layer and pooling layer.
* `nin_p.pth.tar` : The best accurancy model dict for calling pretrained model. 
### model
* `test` : To test whether the model predict correctly.
* `train` : To train the model and adjust the learning rate.
* `valid` : To validate the model and save the best accurancy model in `NIN` floder. 
### test
* Total 20 kinds of fruit with each average 50 photos.
### train
* Total 20 kinds of fruit with each average 200 photos.
### data.py
* Load the images into ImageFolder and split dataset into train & valid dataset.
### main.py
* The main program to run all files according to the `main_argu.py`'s parameter. 
### main_argu.py
* The argument are initialized in this file.

# How To Use
```bash
python3 main.py # generate ./NIN/nin_p.pth.tar
python3 main.py --write --pretrained ./NIN/nin_p.pth.tar --evaluate # writeW2, W8, In8, Bias32, Out8
```
