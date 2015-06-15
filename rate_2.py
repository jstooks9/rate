# dungeons and dragons random terrain generator
# Stooksbury, John
# generate terrain for a dnd quest

import random
import numpy as np
from PIL import Image
from PIL import ImageColor as ic
import sys

inputFileName = sys.argv[1]
with open(inputFileName) as f:
	title = f.readline().split()[0]
	imageSize = f.readline()
	gridSize = f.readline()
	loot = int(f.readline())
	trap = int(f.readline())

GRID_DELIM = 'x'

w = int(imageSize.split(GRID_DELIM)[0])
h = int(imageSize.split(GRID_DELIM)[1])

terrain = np.zeros((w,h,3), dtype=np.uint8)
terrain.shape = h,w,3
terrain.fill(255) # make

terrain[0:100,0:1000] = [255,0,0]

# terrain = Image.frombuffer('RGBA',(w,h),img,'raw','RGBA',0,1)
img_terrain = Image.fromarray(terrain, 'RGB') 
img_terrain.save(title+'.png')