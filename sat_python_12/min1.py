from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
import time

while True:

	x = random.randint(-500, 500)
	y = random.randint(60, 250)
	z = random.randint(-500, 500)

	time.sleep(3)

	mc.player.setTilePos(x, y, z)
