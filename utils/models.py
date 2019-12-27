from torch.nn import CrossEntropyLoss
from torch import optim
from .nadam_optim import Nadam
from torchvision import transforms
from datasets import CustomNormalize

models_conf = {
    'firenet': {
        'img_dims': (64, 64),
        'model_name': 'model_firenet.pth',
        'class_name': 'FireNet',
        'module_name': 'models.firenet_pt',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {'eps': 1e-6},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((64, 64)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((64, 64)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((64, 64)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }
}

models_conf['octfiresnet'] = {
        'img_dims': (96, 96),
        'model_name': 'model_octfiresnet.pth',
        'class_name': 'OctFiResNet',
        'module_name': 'models.octfiresnet',
        'criterion': CrossEntropyLoss(),
        'optimizer': Nadam,
        'optimizer_params': {'lr': 1e-4, 'eps': 1e-7},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((96, 96)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((96, 96)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((96, 96)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }

models_conf['resnet'] = {
        'img_dims': (224, 224),
        'model_name': 'model_resnet.pth',
        'class_name': 'resnet_sharma',
        'module_name': 'models.resnet',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((224, 224)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((224, 224)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((224, 224)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }

models_conf['kutralnet'] = {
        'img_dims': (84, 84),
        'model_name': 'model_kutralnet.pth',
        'class_name': 'KutralNet',
        'module_name': 'models.kutralnet',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': optim.lr_scheduler.StepLR,
        'scheduler_params': { 'step_size':85 }
    }

models_conf['kutralnetoct'] = {
        'img_dims': (84, 84),
        'model_name': 'model_kutralnetoct.pth',
        'class_name': 'KutralNetOct',
        'module_name': 'models.kutralnetoct',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }

models_conf['kutralnet_mobile'] =  {
        'img_dims': (84, 84),
        'model_name': 'model_kutralnet_mobile.pth',
        'class_name': 'KutralNetMobile',
        'module_name': 'models.kutralnet_mobile',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }

models_conf['kutralnet_mobileoct'] = {
        'img_dims': (84, 84),
        'model_name': 'model_kutralnet_mobileoct.pth',
        'class_name': 'KutralNetMobileOct',
        'module_name': 'models.kutralnet_mobileoct',
        'criterion': CrossEntropyLoss(),
        'optimizer': optim.Adam,
        'optimizer_params': {},
        'preprocess_train': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_val': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'preprocess_test': transforms.Compose([
                       transforms.Resize((84, 84)), #redimension
                       transforms.ToTensor()
                    ]),
        'scheduler': None,
        'scheduler_params': {}
    }



def get_config(base_model):
    return models_conf[base_model]

# visualize activations
def plot_filters_single_channel_big(t):

    #setting the rows and columns
    nrows = t.shape[0]*t.shape[2]
    ncols = t.shape[1]*t.shape[3]


    npimg = np.array(t.numpy(), np.float32)
    npimg = npimg.transpose((0, 2, 1, 3))
    npimg = npimg.ravel().reshape(nrows, ncols)

    npimg = npimg.T

    fig, ax = plt.subplots(figsize=(ncols/10, nrows/200))
    imgplot = sns.heatmap(npimg, xticklabels=False, yticklabels=False, cmap='gray', ax=ax, cbar=False)

def plot_filters_single_channel(t):

    #kernels depth * number of kernels
    nplots = t.shape[0]*t.shape[1]
    ncols = 12

    nrows = 1 + nplots//ncols
    #convert tensor to numpy image
    npimg = np.array(t.numpy(), np.float32)

    count = 0
    fig = plt.figure(figsize=(ncols, nrows))

    #looping through all the kernels in each channel
    for i in range(t.shape[0]):
        for j in range(t.shape[1]):
            count += 1
            ax1 = fig.add_subplot(nrows, ncols, count)
            npimg = np.array(t[i, j].numpy(), np.float32)
            npimg = (npimg - np.mean(npimg)) / np.std(npimg)
            npimg = np.minimum(1, np.maximum(0, (npimg + 0.5)))
            ax1.imshow(npimg)
            ax1.set_title(str(i) + ',' + str(j))
            ax1.axis('off')
            ax1.set_xticklabels([])
            ax1.set_yticklabels([])

    plt.tight_layout()
    plt.show()

def plot_filters_multi_channel(t):

    #get the number of kernals
    num_kernels = t.shape[0]

    #define number of columns for subplots
    num_cols = 12
    #rows = num of kernels
    num_rows = num_kernels

    #set the figure size
    fig = plt.figure(figsize=(num_cols,num_rows))

    #looping through all the kernels
    for i in range(t.shape[0]):
        ax1 = fig.add_subplot(num_rows,num_cols,i+1)

        #for each kernel, we convert the tensor to numpy
        npimg = np.array(t[i].numpy(), np.float32)
        #standardize the numpy image
        npimg = (npimg - np.mean(npimg)) / np.std(npimg)
        npimg = np.minimum(1, np.maximum(0, (npimg + 0.5)))
        npimg = npimg.transpose((1, 2, 0))
        ax1.imshow(npimg)
        ax1.axis('off')
        ax1.set_title(str(i))
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])

    plt.savefig('myimage.png', dpi=100)
    plt.tight_layout()
    plt.show()

def plot_weights(model, layer_num, single_channel = True, collated = False):

  #extracting the model features at the particular layer number
  layer = model.features[layer_num]

  #checking whether the layer is convolution layer or not
  if isinstance(layer, nn.Conv2d):
    #getting the weight tensor data
    weight_tensor = model.features[layer_num].weight.data

    if single_channel:
      if collated:
        plot_filters_single_channel_big(weight_tensor)
      else:
        plot_filters_single_channel(weight_tensor)

    else:
      if weight_tensor.shape[1] == 3:
        plot_filters_multi_channel(weight_tensor)
      else:
        print("Can only plot weights with three channels with single channel = False")

  else:
    print("Can only visualize layers which are convolutional")
