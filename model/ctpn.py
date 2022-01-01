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
        
        
calss CTPN(nn.Module):
    
    def __init__(self, pretrained, pretrained_model_path):
        super(CTPN, self).__init__()
        if pretrained:
            if os.exist(pretrained_model_path):
                base_model = torchvision.models.vgg16(pretrained=False)
                base_model.load_state_dict(torch.load(pretrained_model_path))
            else:
                base_model = torchvision.models.vgg16(pretrained=True)
        else:
            base_model = torchvision.models.vgg16()
            
        layers = list(base_model.features)[: -1]
        self.base_layers = nn.Sequential(*layers) # block5_conv3 output
        
        
        
        
        
        
