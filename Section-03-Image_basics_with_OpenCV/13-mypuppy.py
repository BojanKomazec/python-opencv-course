import cv2
img = cv2.imread('../data/00-puppy.jpg')

# cv2.imshow(window_name, matrix)
# https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563
# https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/
cv2.imshow('Puppy', img)

while True:
    # wait 1 ms
    key = cv2.waitKey(1)

    if key == -1:
        continue

    if key == 27:
        print('ESC key has been pressed')
        break

cv2.destroyAllWindows()