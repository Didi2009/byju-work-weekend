import cv2

#load image=>cv2.imread()
img=cv2.imread("butterfly.jpg")
cv2.imshow("display", img)
#print(img)
gray_img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
text_to_show="I like python"
cv2.putText(img, text_to_show, (20, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(255,0,0) )
cv2.imshow("Gray image", gray_img)
cv2.waitKey(0)