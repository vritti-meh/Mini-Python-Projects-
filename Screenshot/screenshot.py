#importing the package
import pyscreenshot

#to capture the screen
image = pyscreenshot.grab()
#for specifying the dimesnions of the captured screenshot
#image2 = pyscreenshot.grab(bbox=(x1,x2,y1,y2))

#to display captured screenshot
image.show()

#to save the screenshot
image.save("firstimg.png")

