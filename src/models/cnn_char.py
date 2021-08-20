from models.tokenizers import charTokenizer
import torch
from torch import nn
from einops import rearrange
from collections import OrderedDict

class CNNconf():
  embedding_size = 128
  fc_hidden = 128
  num_filters = 128
  fc_dropout = 0
  kernel_size = 4
  vocab_size = len(charTokenizer.vocab)
  lr = 1e-3
  checkpoint = "models/weights/ckpt/cnn_char204.ckpt"
  
tokenizer = charTokenizer()

class CNN(nn.Module):
  def __init__(self, config):
    super().__init__()
    self.embedding = nn.Embedding(config.vocab_size, config.embedding_size, padding_idx=0) 
    self.conv = nn.Conv1d(config.embedding_size, config.num_filters, config.kernel_size)
    self.fc1 = nn.Linear(config.num_filters, config.fc_hidden)
    self.do1 = nn.Dropout(config.fc_dropout)      
    self.fc2 = nn.Linear(config.fc_hidden, 1)
    
    self.load_model(config.checkpoint)

  def forward(self, inputs):
    embed = self.embedding(inputs)
    embed = rearrange(embed, "b l e -> b e l")
    conv = self.conv(embed)
    conv = torch.max(conv, dim=-1).values
    fc1 = self.fc1(conv)
    fc1 = self.do1(fc1)
    outputs = self.fc2(fc1)

    return torch.sigmoid(outputs)
  
  def load_model(self, checkpoint):
    ckpt = torch.load(checkpoint, map_location=lambda storage, loc: storage)["state_dict"]
    model_state_dict = OrderedDict([(".".join(k.split(".")[1:]), v) for k, v in ckpt.items()])

    self.load_state_dict(model_state_dict)
      
  def get_info(self):
      pass
      
  def predict(self, inputs, threshold=0.5):
    seq = tokenizer.encode_batch(inputs)
    outputs = self.forward(seq)
    outputs = outputs.squeeze(1).detach().cpu().numpy()
    
    return outputs, None


      
      
      

  
  
