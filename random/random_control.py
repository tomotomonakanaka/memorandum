import random
import torch
import numpy as np
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

random_seed = 1
random.seed(random_seed)
torch.manual_seed(random_seed)
np.random.seed(random_seed)

if device == 'cuda':
    torch.cuda.manualseed_all(random_seed)