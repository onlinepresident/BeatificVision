from PIL import Image
from PIL import ImageEnhance
img_path = 'beatific/img/both.jpg'
color_space = 'RGB-3X8'
# img = Image.open('beatific/img/profile.jpg')
# img.show()
# # img.save('beatific/img/profile_save.png')
#
# dimension  = (100,100,200,200) # image area to crop
# img_crop = img.crop(dimension)
# img_crop.show()


# Color spaces and channels
# 2 types of cordinate system
# cartesian plane (x,y)
# 2-D polar cordinates (r, theta)


# Color spaces
# 1: Red, Blue, Green (RGB)
# 2: Cyan, Magenta, Yellow, Key(black) (CMYK)
# 3: HSV
# 4: HSL
# 5: CMY

# Get image pixel
# img = Image.open('beatific/img/both.jpg')
#
# dimension = (10,15)
# img_pixel = img.getpixel(dimension)
# img.convert('L').getpixel(dimension)



# Convert Image
# img = Image.open('beatific/img/both.jpg')
# img.show()


# img = Image.open(img_path)
# img_gray = img.convert(color_space)
# img_gray.show()


# Geometric Transformation
# #  1: resize image
# img = Image.open(img_path)
# img = img.resize((50,50))
# img.show()

# 2: Roate Image
# img = Image.open(img_path)
# img = img.rotate(360)
# img.show()




# Image Enhancement: contrast, brightness, color balance, or sharpness of an image
# 1: Brightness
# img = Image.open(img_path)
# img = ImageEnhance.Brightness(img)
# img.enhance(2).show()

# 2: Contrast
# img = Image.open(img_path)
# img = ImageEnhance.Contrast(img)
# img = img.enhance(5)
# img.show()
