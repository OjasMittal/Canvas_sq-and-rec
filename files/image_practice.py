import numpy as np
from PIL import Image
data=np.zeros((5,5,3),dtype=np.uint8)
data[:]=[255,120,0]
print(data)
#Indian Flag
data[3:5,0:5]=[0,255,0]
data[2:3,0:5]=[255,255,255]
data[2:3:,2:3]=[0,0,255]

img=Image.fromarray(data,'RGB')
img.save('canvas.png')

