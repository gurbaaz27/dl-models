# Deep Learning Models
Under the summer project at my institute **IIT Kanpur** "Model Zoo", we are learning and practising to implement and summarise various deep learning architectures and models.

Here is a list of the implemenations:
1. **Resnet** : [Original Paper](https://arxiv.org/abs/1512.03385) (*Implemented*)
   * Based on CNN, aimed to tackle the difficulty of training deeper networks without rise in training and testing error.
2. **InfoGAN** : [Original Paper](https://arxiv.org/abs/1606.03657) (*Implemented*)
   * Based on DCGan, aimed at disentangled representation so that network learns systematically various meaningful features of      the input sample. 
3. **ALBERT** : [Original Paper](https://arxiv.org/abs/1909.11942) (*Under implementation*)
   * Based on BERT, it addresses the GPU/TPU memory limitations and training complexities of the the former by proposing two        parameter-reduction techniques, which lowers memory, increases training speed and even achieves greater accuracy. 
4. **Image Captioning** : [Original Paper](https://cs.stanford.edu/people/karpathy/cvpr2015.pdf) (*Implemented*)
    * Based on a novel combination of CNN over images and bidirectional RNN (LSTM) over captions, using output of encoder CNN as embeddings for the decoder RNN to generate
rich descriptions of image regions.
