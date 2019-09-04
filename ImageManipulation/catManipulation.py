from PIL import Image

catImg = Image.open('zophie.png')

#This will print the size of the image in pixels
print(catImg.size)

#This will give the width and height variables what's stored in the .size object
width, height = catImg.size

#This will print the format of the picture
print(catImg.format)
print(catImg.format_description)

#This will save the picture to a .jpg file 
catImg.save('zophie.jpg')

#This will crop and image and make a new file for it
croppedImg = catImg.crop((335, 345, 565, 560))
croppedImg.save('cropped.png')