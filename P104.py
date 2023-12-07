import cv2

img = cv2.imread('C:/Users/pidik/Downloads/PRO-104-OpenCV-Image-Assets-main/PRO-104-OpenCV-Image-Assets-main/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg')

cv2.putText(img,'Sun',(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,'Mercury',(120,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Venus',(180,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Earth',(290,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Mars',(400,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Jupiter',(550,70),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Saturn',(780,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Uranus',(950,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))
cv2.putText(img,'Neptune',(1100,130),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0))


cv2.imshow('output',img)

cv2.waitKey(5000)

cv2.imwrite('Solar_systemwithname.jpg',img)
