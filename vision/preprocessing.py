img_path = 'beatific/img/both.jpg'
color_space = 'RGB-3X8'

from PIL import Image
from PIL import ImageEnhance

# character recognition ML Model
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from skimage import io, color, feature, transform


#step 2: convert the image
# training the model. 75% of the data will be used to train the model. 25% to test the Model






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
# img = img.enhance(2)
# img.show()


#
mnist = datasets.load_digits()
images = mnist.images
size =len(images)

#  image data preprocessing
images = images.reshape(size, -1)
labels = mnist.target

# initializethe  Logistic Regression classifier
lr_classifier = LogisticRegression(C=0.01, penalty='l1', tol=0.01,solver='liblinear')
lr_classifier.fit(images[:int((size / 4) * 3)], labels[:int((size / 4) * 3)])

# testing the model with user (custom) images
#step 1: load the image
img_user = io.imread(img_path)

# convert image to gray scale to be able to handle well
img_user = color.rgb2gray(img_user)

# resize the image to 28 x 28. this is the dimension the model was trained on
img_user = transform.resize(img_user,(8,8), mode='wrap')

# run edge detection on the image
img_user=feature.canny(img_user,sigma=5)
img_user = img_user.flatten()

prediction = lr_classifier.predict(img_user)
print(prediction)
