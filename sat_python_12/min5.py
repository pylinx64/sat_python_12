from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
block = 46

mc.setBlock(x, y-1, z, block)
