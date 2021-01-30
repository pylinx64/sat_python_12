from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = -22
y = 64
z = -53
block = 46

while y < 255:
	time.sleep(1)
	mc.setBlock(x, y, z, block)
	y = y + 1
