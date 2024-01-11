import numpy as np
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
import pytesseract
from tensorflow.keras.preprocessing.image import load_img,img_to_array
model=tf.keras.models.load_model('./static/models/object_detection_latest.h5')

def object_detection(path,filename):
    
        image=load_img(path)
        image=np.array(image,dtype=np.uint8)#8 bit arrays
        image1=load_img(path,target_size=(224,224))
        image_arr_224=img_to_array(image1)/255#divide for normalising
        h,w,d=image.shape
        test_arr=image_arr_224.reshape(1,224,224,3)
        #predicting
        coords=model.predict(test_arr)
        denorm=np.array([w,w,h,h])
        coords=coords*denorm
        coords=coords.astype(np.int32)
        xmin,xmax,ymin,ymax=coords[0]
        pt1=(xmin,ymin)
        pt2=(xmax,ymax)
        print(pt1,pt2)
        cv2.rectangle(image,pt1,pt2,(0,255,0),3)
        image_bgr=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        cv2.imwrite('./static/predict/{}'.format(filename),image_bgr)
        return coords
def characters(path,filename):
    img=np.array(load_img(path))
    coordinates=object_detection(path,filename)
    xmin,xmax,ymin,ymax=coordinates[0]
    numberplate_region=img[ymin:ymax,xmin:xmax]
    numberplate_region=cv2.cvtColor(numberplate_region,cv2.COLOR_RGB2BGR)
    cv2.imwrite('./static/numberplate region/{}'.format(filename),numberplate_region)
    text=pytesseract.image_to_string(numberplate_region)
    print(text)
    return text
