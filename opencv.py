import numpy as np
import cv2
import tensorflow as tf
import tensorflow.keras as keras
m_new = tf.keras.models.load_model('mnist (1).h5')

img = np.ones([400,400],dtype ='uint8')*255

img[50:350,50:350]=0
wname = 'Canvas'
cv2.namedWindow(wname)
def shape(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        print(x,y)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),10,(255,0,0),-1)
        print(x,y)

cv2.setMouseCallback(wname,shape)  # Shape is a sub method called in the setMouseCallback method

while True:
    cv2.imshow(wname,img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        img[50:350,50:350]=0
    elif key == ord('w'):
        out = img[50:350,50:350]
        cv2.imwrite('Output.jpg',out)
        z = m_new.predict_clases(image_test_resize)
        print(m_new)
        
cv2.destroyAllWindows()



# Mouse Events
#  LEFT, RIGHT, DOUBLE LEFT
