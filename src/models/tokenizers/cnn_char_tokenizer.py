import torch
from collections import defaultdict

class charTokenizer():
  vocab = " .0123456789/:abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?#&àáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ"
  maxlen = 128

  def __init__(self):
    self.char2int = defaultdict(int)
    self.int2char = defaultdict(int)
    self.vocab_size = len(charTokenizer.vocab)

    self._init_vocab()
  def _init_vocab(self):
    for idx, c in enumerate(charTokenizer.vocab):
      # 0 mean Padding 
      self.char2int[c] = idx + 1
    
    for c, idx in self.char2int.items():
      self.int2char[idx] = c

    self.int2char[0] = ""

  def encode(self, text):
    if(isinstance(text, str)):
      encode_text = [self.char2int[c] for c in text]
      return encode_text
    else:
      raise TypeError('invalid type text')

  def decode(self, seq):
    text = ""

    if(isinstance(seq, torch.Tensor)):
      seq = seq.detach().numpy()
    for idx in seq:
      text += str(self.int2char[idx])
    return text
  
  def truncate(self, seq):
    return seq[:charTokenizer.maxlen]
    #return seq

  def padding(self, seq):
    return seq + [0] * (charTokenizer.maxlen - len(seq))

  def preprocess(self, seq):
    if len(seq) > charTokenizer.maxlen:
      seq = self.truncate(seq)
    elif len(seq) < charTokenizer.maxlen:
      seq = self.padding(seq)
    
    return seq

  def encode_batch(self, data):    
    if(isinstance(data, str)):
      data = [data]
    
    encode_seq = [self.encode(text) for text in data]
    encode_seq = [self.preprocess(seq) for seq in encode_seq]

    encode_tensor = torch.Tensor(encode_seq).type(torch.int32)
    #print(encode_tensor)
    return encode_tensor

  def decode_batch(self, seqs):
    if(isinstance(seqs, torch.Tensor)):
      seqs = seqs.detach().numpy()

    decode_seq = [self.decode(seq) for seq in seqs]
    return decode_seq