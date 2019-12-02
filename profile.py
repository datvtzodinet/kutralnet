import torch
from thop import profile, count_hooks, clever_format
from models.firenet_pt import FireNet
from models.octfiresnet import OctFiResNet
from models.resnet import resnet_sharma

model = FireNet(classes=2)
input = torch.randn(1, 3, 64, 64)
flops, params = profile(model, verbose=False,
        inputs=(input, ),
        custom_ops={torch.nn.Dropout2d: None})
flops, params = clever_format([flops, params], "%.3f")
print('FireNet 64x64 flops, params', flops, params)

model = OctFiResNet(classes=2)
input = torch.randn(1, 3, 64, 64)
flops, params = profile(model, verbose=False,
        inputs=(input, ),
        custom_ops={torch.nn.Dropout2d: None})
flops, params = clever_format([flops, params], "%.3f")
print('OctFiResNet 64x64 flops, params', flops, params)

model = resnet_sharma(num_classes=2)
input = torch.randn(1, 3, 224, 224)
flops, params = profile(model, verbose=False,
        inputs=(input, ),
        custom_ops={torch.nn.Dropout2d: None})
flops, params = clever_format([flops, params], "%.3f")
print('ResnetMod 224x224 flops, params', flops, params)