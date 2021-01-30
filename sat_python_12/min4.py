from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.player.getTilePos()
x = pos.x - 2
y = pos.y - 1
z = pos.z - 2

l = 20
w = 20

block = 41

mc.setBlocks(x, y, z, x + l, y, z + w, block)

while True:
	if block == 41:
		block = 57
	elif block == 57:
		block = 41 
	mc.setBlocks(x, y, z, x + l, y, z + w, block)
	time.sleep(0.3)
