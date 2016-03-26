from PIL import Image
from PIL import ImageFilter

img = Image.open("ic_launcher.png")
asd = Image.open("Screen Shot.png")
print(img.size)
print(img.format)

area = (100, 100, 612, 612)
cropped_img = img.crop(area)
# img.show()
# cropped_img.show()

asd.paste(img,area)
# asd.show()

asd1 = Image.open("666.jpg")
asd2 = Image.open("865.jpg")
print(asd1.mode)
r,g,b,a = asd1.split()
r1,g1,b1,a = asd2.split()

# r.show()
# g.show()
# b.show()
# a.show()

new_img = Image.merge("RGB",(r1,g,b1))
# new_img.show()


square = img.resize((400,400))
flip = img.transpose(Image.FLIP_LEFT_RIGHT)
spin = img.transpose(Image.ROTATE_90)
# square.show()
# flip.show()
# spin.show()

black_white = asd1.convert("L")
# black_white.show()

black_white = asd1.convert("L")

blur = asd1.filter(ImageFilter.BLUR)
blur.show()

detail = asd1.filter(ImageFilter.DETAIL)
edgles = asd1.filter(ImageFilter.FIND_EDGES)
detail.show()
edgles.show()



