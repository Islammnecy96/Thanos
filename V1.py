import os
import random
from random import sample

g=os.listdir(r"C:\Users\MaRkZ\Desktop\AI\LEC 4\Universe")

for i in sample(g,1):
    os.remove(os.path.join(r"C:\U sers\MaRkZ\Desktop\AI\LEC 4\Universe", i))
