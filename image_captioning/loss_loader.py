import torch
import os
import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-model',type=str,default='resnet18')
    args = parser.parse_args()
    print(args)

    model_name = args.model
    print('Training Loss data:')
    training_loss = torch.load(os.path.join(model_name, 'training_loss.pt'))
    print(training_loss.data)

    print('Validation Loss data:')
    validation_loss = torch.load(os.path.join(model_name, 'validation_loss.pt'))
    print(validation_loss.data)
