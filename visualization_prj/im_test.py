import matplotlib.pyplot as plt
from PIL import Image
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg')
if image1.height != image2.height:
    pass
else:
    new_width = image1.width + image2.width
    new_image = Image.new('RGB',(new_width,image1.height))
    new_image.paste(image1,(0,0))
    new_image.paste(image2, (image1.width, 0))
    new_image.save('combined_image.jpg')
class im_show:
   def __init__(self,url):
         self.url = url

   def show(self):
       image = Image.open(self.url)
       fig, ax = plt.subplots()
       ax.imshow(image)
       ax.axis('off')
       plt.show()

show_todo = im_show('combined_image.jpg')
show_todo.show()