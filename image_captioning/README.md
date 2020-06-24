# PyTorch implementation of Image Captioning [*Paper*](https://cs.stanford.edu/people/karpathy/cvpr2015.pdf)

## Usage 

### 1. Preprocessing the data
* Dataset used is Flickr8k ([*download here*](https://www.kaggle.com/shadabhussain/flickr8k)). 
* Extract and move images to a folder named : images and text files to folder named : text
> ***NOTE** : Place both folders alongside the python files.*
* Run the following command in Windows : 
      <pre><code>python preprocess.py
      </code></pre>
      If using Linux/Mac use : 
      <pre><code>python3 preprocess.py
      </code></pre>
      
### 2. Training the data
* Run the following command : 
      <pre><code>python train.py -model <encoder_CNN_architecture> -dir <train_dir_path> -save_epoch <model_checkpoint> -learning_rate <learning_rate> -num_epoch <num_epoch> -hidden_dim <lstm_hidden_state_dim> -embedding_dim <encoder_CNN_output>
      </code></pre>
> ***NOTE** : Use python3 instead in case of Linux/Mac .*
* Arguments
  * -model : Default: 'resnet18', other option is 'inception' (Inception_v3).
  * -dir : Training Directory path, default: 'train'
  * -save_epoch : Epochs after which model saves checkpoint, default : 2
  * -learning_rate : Adam optimizer learning rate, default : 1e-3 (0.001)
  * -num_epoch : Number of epochs, default : 10
  * -hidden_dim : Dimensions in hidden state of LSTM decoder, default : 512
  * -embedding_dim : Dimensions of encoder output, default : 512

### 3. Testing the model
* Run the following command : 
    <pre><code>python test.py -model <encoder_CNN_architecture> -image_path <image_path> -epoch <epoch_num></code></pre>
> ***NOTE** : Once again, use python3 instead in case of Linux/Mac .*
* Arguments
  * -model : Default: 'resnet18', other option is 'inception' (Inception_v3).
  * -image_path : Image Directory path to test caption generation, default: 'test'
  * -epoch : Trained model to be used after this many epochs.
  
### 4. Validation 
* Run the following command : 
    <pre><code>python train.py -model <encoder_CNN_architecture> -dir <dev_dir_path> -save_epoch <model_checkpoint> -num_epoch <num_epoch></code></pre>
> ***NOTE** : For last time, use python3 instead in case of Linux/Mac :).*
* Arguments
  * -model : Default: 'resnet18', other option is 'inception' (Inception_v3).
  * -dir : Development Directory path, default: 'dev'
  * -save_epoch : Epochs after which model saves checkpoint, default : 2
  * -num_epoch : Number of epochs, default : 10
> ***NOTE** : The save_epoch and num_epoch should match with your corresponding training model .*

## Factual Details
- **Title** : Deep Visual-Semantic Alignments for Generating Image Descriptions
- **Dated** : 2015
- **Authors** : Andrej Karpathy, Li Fei-Fei
- **University** : Department of Computer Science, Stanford University
- **Field** : Deep Learning, NLP, CNN, Image Captioning

## Contributed by
- [*Gurbaaz Singh Nandra*](https://github.com/gurbaaz27)

# Summary

## A Gentle Intoduction : Why ? 


## Results :
* Training time :
<pre><code>Epoch : 0 , Avg_loss = 3.141907, Time = 9.89 mins
Epoch : 1 , Avg_loss = 2.978030, Time = 9.89 mins
Epoch : 2 , Avg_loss = 2.879061, Time = 9.88 mins
Epoch : 3 , Avg_loss = 2.800483, Time = 9.90 mins
Epoch : 4 , Avg_loss = 2.734463, Time = 9.88 mins
Epoch : 5 , Avg_loss = 2.676081, Time = 9.90 mins
Epoch : 6 , Avg_loss = 2.625130, Time = 9.89 mins
Epoch : 7 , Avg_loss = 2.579518, Time = 9.90 mins
Epoch : 8 , Avg_loss = 2.538572, Time = 9.90 mins
Epoch : 9 , Avg_loss = 2.501715, Time = 9.90 mins
      </code></pre>
<p align="center">
  <img width="697" height="398" src="assets/training_loss.JPG">
</p>
> ***NOTE** : Here loss plotted is total loss of dataset, which is for 6000 X 5 = 30000 captions. Mean loss is loss plotted divided by 30000 .*

* Testing time : 
 <pre><code><start> a man in a black shirt and blue pants is playing a guitar . <end></code></pre>
 <p align="center">
  <img width="986" height="535" src="assets/test1.jpg">
</p>

* Validation time :
<pre><code>
      </code></pre>
<p align="center">
  <img width="697" height="398" src="assets/validation_loss.JPG">
</p>

 
## Acknowledgement
- [Medium : Captioning Images with CNN and RNN, using PyTorch](https://medium.com/@stepanulyanin/captioning-images-with-pytorch-bc592e5fd1a3)
- [Word Embeddings](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)

