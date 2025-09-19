import cv2
from matplotlib import pyplot as plt
import random
import math
import numpy as np

def rotation():
    
    image1 = cv2.imread("./test_image.jpg")
    
    rad = 20 * math.pi / 180 # 각도 설정
    
    # np.array로 Affine 행렬 생성
    affin = np.array([[math.cos(rad), math.sin(rad), 0],
                      [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)
    
    result = cv2.warpAffine(image1, affin, (0,0))
    
    # image 출력
    cv2.imshow('original', image1)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    
    return 0

rotation()