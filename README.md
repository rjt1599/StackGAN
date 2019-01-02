**This repository is forked and slightly modified from the original repository of the StackGan [authors](https://github.com/hanzhanggit/StackGAN), as per the code in the book [Learning Generative Adversarial Network](https://github.com/Kuntal-G/Books/tree/master/Learning-Generative-Adversarial-Network/)**.


The original codebase is built with older tensorflow version (0.11).
So inorder to compile or run the run using pre-trained models you need to have tensorflow version below 1.0 on your machine. You can modify your tensorflow version using: 
sudo pip install tensorflow==0.12.0



# Note: 
1) I'm updating this codebase to make it compatible with Tensorflow version 1.2.0 or above -- * Work in Progress *

2) While running some of the python scripts mentioned below,if you face any module import error (No module found), then set the following two lines in the script:
```
import sys
sys.path.insert(0, '<path to this project') 

for example: sys.path.insert(0, '/home/kuntalg/StackGAN') 
```


# StackGAN

Tensorflow implementation for reproducing main results in the paper [StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks](https://arxiv.org/pdf/1612.03242v1.pdf) by Han Zhang, Tao Xu, Hongsheng Li, Shaoting Zhang, Xiaogang Wang,   Xiaolei Huang, Dimitris Metaxas.


<img src="examples/framework.jpg" width="850px" height="370px"/>


### Dependencies
python 2.7

[TensorFlow 0.12](https://www.tensorflow.org/get_started/os_setup)
Currently the code is compatible with an older version of TensorFlow
(0.12), so you need to have TensorFlow version below 1.0 to successfully
run this code. You can modify your TensorFlow version using: 

`sudo pip install tensorflow==0.12.0.`

In addition, please install following packages:
- `prettytensor`
- `progressbar`
- `python-dateutil`
- `easydict`
- `pandas`
- `torchfile`
- `requests`

#### Install using pip
`sudo pip install prettytensor progressbar python-dateutil easydict pandas torchfile requests`


**Data**

1. Download the preprocessed char-CNN-RNN text embeddings for [birds] and 
save them to `Data/`.

`python google-drive-download.py 0B3y_msrWZaXLT1BZdVdycDY5TEE Data/birds.zip`

Extract them inside `Data/birds/` directory respectively.

`unzip Data/birds.zip`
  
  
2. Download the [birds](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html) image data. 

`wget http://www.vision.caltech.edu/visipedia-data/CUB-200-2011/CUB_200_2011.tgz -O Data/birds/CUB_200_2011.tgz`


Extract them inside `Data/birds/` directory respectively.

`tar -xzf CUB_200_2011.tgz`

3. Preprocess images for birds: `python misc/preprocess_birds.py`


**Pretrained Model**
- Download the pre-trained char-CNN-RNN text embedding model trained and save it to `models/`.

`python google-drive-download.py 0B3y_msrWZaXLNUNKa3BaRjAyTzQ models/ birds_model_164000.ckpt`


- Also download the char-CNN-RNN text encoder for birds and save it under the models/text_encoder directory.

`python google-drive-download.py 0B0ywwgffWnLLU0F3UHA3NzFTNEE models/text_encoder/  lm_sje_nc4_cub_hybrid_gru18_a1_c512_0.00070_1_10_trainvalids.txt_iter30000.t7
`


**Run Demos**

- Add following lines in the example_captions.txt file

`A white bird with a black crown and red beak
this bird has red breast and yellow belly`


- Run `sh demo/birds_demo.sh` to generate bird samples from sentences. The results will be saved to `Data/birds/example_captions/`.





