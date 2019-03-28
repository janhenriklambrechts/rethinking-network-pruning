
import torch
print("=> loading checkpoint")
checkpoint = torch.load('checkpoint.pth.tar')
start_epoch = checkpoint['epoch']
best_prec1 = checkpoint['best_prec1']
for i in best_prec1:
    print(i)