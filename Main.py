from nbt import nbt



SIZE = 128
GRID_SIZE = 10
BaseMapMultipliers = [180, 220, 255, 135]
BaseMapColors = [ 
    [0, 0, 0, 0],
    [127, 178, 56],
    [247, 233, 163],
    [199, 199, 199],
    [255, 0, 0],
    [160, 160, 255],
    [167, 167, 167],
    [0, 124, 0],
    [255, 255, 255],
    [164, 168, 184],
    [151, 109, 77],
    [112, 112, 112],
    [64, 64, 255],
    [143, 119, 72],
    [255, 252, 245],
    [216, 127, 51],
    [178, 76, 216],
    [102, 153, 216],
    [229, 229, 51],
    [127, 204, 25],
    [242, 127, 165],
    [76, 76, 76],
    [153, 153, 153],
    [76, 127, 153],
    [127, 63, 178],
    [51, 76, 178],
    [102, 76, 51],
    [102, 127, 51],
    [153, 51, 51],
    [25, 25, 25],
    [250, 238, 77],
    [92, 219, 213],
    [74, 128, 255],
    [0, 217, 58],
    [129, 86, 49],
    [112, 2, 0],
    [209, 177, 161],
    [159, 82, 36],
    [149, 87, 108],
    [112, 108, 138],
    [186, 133, 36],
    [103, 117, 53],
    [160, 77, 78],
    [57, 41, 35],
    [135, 107, 98],
    [87, 92, 92],
    [122, 73, 88],
    [76, 62, 92],
    [76, 50, 35],
    [76, 82, 42],
    [142, 60, 46],
    [37, 22, 16],
    [189, 48, 49],
    [148, 63, 97],
    [92, 25, 29],
    [22, 126, 134],
	[58, 142, 140],
	[86, 44, 62],
	[20, 180, 133],
	[100, 100, 100],
	[216, 175, 147],
	[127, 167, 150]
]


class MinecraftMap:
    def __init__(self):
        self.colors = [[[] for _ in range(SIZE)] for _ in range(SIZE)]

        self.currX = 0
        self.currY = 0

    def addColor(self, id):

        r = int(BaseMapColors[int(id / 4)][0] * BaseMapMultipliers[id % 4] / 255.0)
        g = int(BaseMapColors[int(id / 4)][1] * BaseMapMultipliers[id % 4] / 255.0)
        b = int(BaseMapColors[int(id / 4)][2] * BaseMapMultipliers[id % 4] / 255.0)


        self.colors[self.currX][self.currY] = [r, g, b]
        self.currX += 1
        if self.currX == SIZE:
            self.currX = 0
            self.currY += 1

maps = []
numMaps = 50

for i in range(numMaps):
    map = MinecraftMap()

    nbtFile = nbt.NBTFile("Maps/map_" + str(i) + ".dat", "rb")

    colors = nbtFile["data"]["colors"]

    for i in range(len(colors)):
        map.addColor(colors[i])

    maps.append(map)





# nbtFile = nbt.NBTFile("Maps/map_1.dat", "rb")

# print(nbtFile.pretty_tree())

# #get the colors attribute
# colors = nbtFile["data"]["colors"]


#add each color to the map

# map = MinecraftMap()

# for i in range(len(colors)):
#     map.addColor(colors[i])
    # if colors[i] == 0:
    #     print("0 at " + str(i))

# use pygame to display the map
import pygame
pygame.init()
screen = pygame.display.set_mode((SIZE * GRID_SIZE, SIZE * GRID_SIZE))
pygame.display.set_caption("Map")
clock = pygame.time.Clock()

#instead of showing only 1 map at a time, scroll through all of them

currentMap = 0
xOffset = 0

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xOffset += 5

    if xOffset == SIZE * GRID_SIZE:
        xOffset = 0
        currentMap += 1

    
    for x in range(SIZE):
        for y in range(SIZE):
            pygame.draw.rect(screen, maps[currentMap].colors[x][y], (x * GRID_SIZE - xOffset, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    
    for x in range(SIZE):
        for y in range(SIZE):
            pygame.draw.rect(screen, maps[currentMap + 1].colors[x][y], (x * GRID_SIZE - xOffset + GRID_SIZE * SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))


    pygame.display.flip()

pygame.quit()


