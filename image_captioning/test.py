import os
import torch
import pickle
import argparse
from PIL import Image
#------------------------
import torch
import torch.nn as nn
from cnn_model import get_CNN
from decoder import RNN
from vocab import Vocabulary
from torchvision import transforms
from dataloader import DataLoader, shuffle_data
#--------------------------
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-model',type=str,default='resnet18')
    parser.add_argument('-image_path',type=str,default='test')
    parser.add_argument('-epoch',type=int)

    args = parser.parse_args()
    print(args)

    f = open(os.path.join(model_name, 'vocab.pkl'), 'rb')
    vocab = pickle.load(f)

    transform = transforms.Compose([transforms.Resize((224, 224)),
	                                transforms.ToTensor(),
	                                transforms.Normalize((0.5, 0.5, 0.5),
	                                                     (0.5, 0.5, 0.5))
	                                ])
	image = transform(Image.open(args.image_path))
    vocab_size = vocab.index
    embedding_dim = 512
    hidden_dim = 512
    model_name = args.models
    epoch = args.epoch

    cnn = get_CNN(architecture= model_name, embedding_dim=embedding_dim)
    lstm = RNN(embedding_dim=embedding_dim,hidden_dim=hidden_dim,vocab_size=vocab_size)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    cnn.to(device)
    lstm.to(device)
    image = image.unsqueeze(0)
    image = image.to(device)

    cnn_filename = 'epoch_' + epoch + '_cnn.pkl'
    lstm_filename = 'epoch_' + epoch + '_lstm.pkl'

    cnn.load_state_dict(torch.load(os.path.join(model_name, cnn_filename)))
    lstm.load_state_dict(torch.load(os.path.join(model_name, lstm_filename)))

    cnn_output = cnn(image)
    ids_list = lstm.greedy(cnn_output)
    print(vocab.get_sentence(ids_list))
