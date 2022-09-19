import cv2
import argparse
import numpy as np
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", "-n", help="name of the image", default=None)
    args = parser.parse_args()

    name_of_img = args.name
    assert name_of_img != None

    # parameters        
    c1 = (201, 255, 245)    # light colour
    c2 = (163, 151, 86)     # medium colour
    c3 = (34, 30, 161)      # dark colour

    # load image and smooth by Gaussian Blur
    img = cv2.imread(f"./img/{name_of_img}.jpg")
    img = cv2.GaussianBlur(img, (3,3), 10)
    img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

    # covert to gray scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    HEIGHT, WIDTH = gray_img.shape

    # choose color depends on gray scale value
    new_img = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8)
    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            if gray_img[i][j] < 100:
                new_img[i][j] = c3
            elif gray_img[i][j] < 200:
                new_img[i][j] = c2
            else:
                new_img[i][j] = c1
    
    cv2.imshow("origin", img)
    cv2.imshow("Posterize", new_img)
    cv2.waitKey(0)

    if not os.path.exists("posterize"):
        os.makedirs("posterize")
    
    # save image
    cv2.imwrite(f"./posterize/{name_of_img}.jpg", new_img)

    # get edge
    canny_img = cv2.Canny(new_img, 50, 100)
    cv2.imshow("Canny", canny_img)
    cv2.waitKey(0)

    if not os.path.exists("canny"):
        os.makedirs("canny")
    
    # save image
    cv2.imwrite(f"./canny/{name_of_img}.jpg", canny_img)