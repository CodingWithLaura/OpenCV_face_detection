#! /bin/python
import numpy as np
import cv2

def sobel_filter(img):
    sobel_matrix = [[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]]
    
    y_length = img.shape[1]
    x_length = img.shape[0]

    sobeled_img = np.zeros((x_length, y_length, 1), dtype = "uint8")
    
    for y in range(1, y_length-3):
        for x in range(1, x_length-3):
            sobeled_img[x-1][y-1] = ( sobel_matrix[0][0]*img[x-1][y-1] + sobel_matrix[0][1]*img[x][y-1] +  sobel_matrix[0][2]*img[x+1][y-1] +
                                      sobel_matrix[1][0]*img[x-1][y]   + sobel_matrix[1][1]*img[x][y] +  sobel_matrix[1][2]*img[x+1][y] +
                                      sobel_matrix[2][0]*img[x-1][y+1] + sobel_matrix[2][1]*img[x][y+1] +  sobel_matrix[2][2]*img[x+1][y+1])
    return sobeled_img

cap = cv2.VideoCapture(0)
while True:
#    ret, img = cap.read(0)
    img = cv2.imread('sonneborn.jpg')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray_img, threshold1=30, threshold2=100) 
    convolution_img = sobel_filter(gray_img)
    cv2.imshow('orginal', img)
    cv2.imshow('Gray image', gray_img)
    cv2.imshow('canny detection', edges)
    cv2.imshow('matschbild',convolution_img)
    if 0xFF & cv2.waitKey(5) == 27:
        break
cv2.destroyAllWindows()
