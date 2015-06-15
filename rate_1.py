# dungeons and dragons random terrain generator
# Stooksbury, John
# generate terrain for a dnd quest

import sys
import random
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------
# Procedures

def place_items(x,ss,image,val):
	# x is a number of objects to be placed
	# ss are the start and end of the range
	locations = []
	for e in range(x):
		locations.append(random.randint(ss[0],ss[1]))
	i = 0
	for x in np.nditer(image, op_flags=['readwrite']):
		if i in locations:
			x[...] = val
		i += 1

# ------------------------------------------------------

inputFileName = sys.argv[1]

with open(inputFileName) as f:
	gridSize = f.readline()
	loot = int(f.readline())
	trap = int(f.readline())

GRID_DELIM = 'x'
# black = [256,256,256]
terrainMatrix = np.zeros([int(gridSize.split(GRID_DELIM)[0]),
							int(gridSize.split(GRID_DELIM)[1])])
# terrainMatrix = np.array([int(gridSize.split(GRID_DELIM)[0])*black,
# 							int(gridSize.split(GRID_DELIM)[1]*black)])

terrainSize = np.size(terrainMatrix)
locLimits = [0,terrainSize]

# for x in np.nditer(terrainMatrix, op_flags=['readwrite']):
# 	if random.random() > 0.5:
# 		x[...] = 10

place_items(loot,locLimits,terrainMatrix,random.random())
place_items(trap,locLimits,terrainMatrix,random.random())

plt.imshow(terrainMatrix)
# plt.grid()
plt.show()