import cv2  ##pip intall opencv-python

    # How to Show image in python
# -----------------------------------------------------------------------
# # First we need to read the image
# img=cv2.imread('My image.jpeg')
# # Show image
# cv2.imshow('My image',img)
# # Throught this line we can see our image
# cv2.waitKey(0)  # in waitKey "k" must be Capital

     # The  Main program starts from here
# --------------------------------------------------------------------------

# # First we need to read the image
img=cv2.imread('My image.jpeg')
# show image
cv2.imshow('My image',img)
## Here we are specifying percentage to resize the image
percent=50
## specify width and height
width=int(img.shape[1]*percent/100)
height=int(img.shape[0]*percent/100)
## here we resize the image
output=cv2.resize(img,(width,height))
## here we give the destination where we want to save our image
cv2.imwrite('My image resized.jpeg',output)
## Through this line we are able to see the image
cv2.waitKey(0)