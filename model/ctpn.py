import pytorch 
import pytorch.nn as nn
import torchvision.models as models
import os

class BiLSTM(nn.Module):
    
    def __init__(self, in_planes, nums_units, out_planes):
        super(BiLSTM, self).__init__()
        self.lstm = nn.LSTM(in_planes, nums_units, bidirectional=True)
        self.fc = nn.Linear(nums_units * 2, out_planes)
        
    def forward(self, x):
        out, _ = self.lstm(x)
        NH, W, C = out.size()
        out = out.view(NH * W, C)
        out = self.fc(out)
        out = out.view(NH, W, -1)
        return out
        
        
        
        
