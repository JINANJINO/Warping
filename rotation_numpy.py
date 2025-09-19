import numpy as np
import cv2

# 
def rotate_image_remap(img, angle_deg):

    H, W = img.shape[:2]
    cx, cy = (W - 1) / 2.0, (H - 1) / 2.0

    # 출력 좌표 그리드 (x,y)
    out_W, out_H = W, H
    out_cx, out_cy = cx, cy

    xs = np.arange(out_W, dtype=np.float32)
    ys = np.arange(out_H, dtype=np.float32)
    X, Y = np.meshgrid(xs, ys)  # (out_H, out_W)

    # to-do
     # 중심 기준 좌표
    x_c = X - out_cx
    y_c = Y - out_cy

    # 회전 각도 (라디안)
    theta = np.deg2rad(angle_deg)
    cos_t, sin_t = np.cos(theta), np.sin(theta)

    # 역회전 적용 (출력 → 입력 좌표)
    x_src =  cos_t * x_c + sin_t * y_c
    y_src = -sin_t * x_c + cos_t * y_c

    # 원래 좌표계로 이동
    map_x = x_src + cx
    map_y = y_src + cy
    
    # remap 수행
    rotated = cv2.remap(
        img,
        map_x.astype(np.float32), map_y.astype(np.float32),
        interpolation=cv2.INTER_NEAREST,
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0,0,0)
    )
    return rotated

# 사용 예시
if __name__ == "__main__":
    img = cv2.imread("./test_image.jpg")
    rot1 = rotate_image_remap(img, 30)
    cv2.imshow('original', img)
    cv2.imshow('result', rot1)
    cv2.waitKey(0)
    #cv2.imwrite("result.jpg", rot1)