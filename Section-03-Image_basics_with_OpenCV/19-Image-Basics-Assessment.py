import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('../data/dog_backpack.jpg')
print(type(img))
print(img.shape)

# fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
fix_img = img

winname = 'mouse_draw_circles'

# mouse event callback - must conform to cv2::MouseCallback signature
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(fix_img, (x, y), 100, (0, 0, 255), 2) # red circle

cv2.namedWindow(winname)
cv2.setMouseCallback(winname, draw_circle)

# Show image with OpenCV


while True:
    cv2.imshow(winname, fix_img)
    # press ESC to close the window; don't use close button [x]
    if cv2.waitKey(20) & 0xFF == 27:
        break;

cv2.destroyAllWindows()