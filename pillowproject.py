import PIL
from PIL import Image
im = Image.open("/Users/huangzhehao/Desktop/TRUST ME I'm an Engineer/Python/Lenna.jpg")
r, g, b = im.split()
zero = Image.new("L", im.size, color=0)
im.show()
#red
im = Image.merge("RGB", (r, zero, zero))
im.show()
#green
im = Image.merge("RGB", (zero, g, zero))
im.show()
#blue
im = Image.merge("RGB", (zero, zero, b))
im.show()
#og greyscale
im=Image.open("/Users/huangzhehao/Desktop/TRUST ME I'm an Engineer/Python/Lenna.jpg")
im = im.convert("L")
im.show()
#bluish rgb
im=Image.open("/Users/huangzhehao/Desktop/TRUST ME I'm an Engineer/Python/Lenna.jpg")
r, g, b = im.split()
b = b.point(lambda v: 150 + v * 105 / 255)
im = Image.merge("RGB", (r, g, b))
im.show()
#bluish greyscale
im = im.convert("L")
im.show()