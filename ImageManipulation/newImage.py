from PIL import Image

#This will create a new purple image
img = Image.new('RGBA', (100, 200), 'purple')
img.save('purpleImage.png')

#This will make a 20x20 transparent image
img2 = Image.new('RGBA', (20,20))
img2.save('transparentImage.png')