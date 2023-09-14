import cv2
img = cv2.imread('Aayush_DIP.jpg', 0)

print("image shape = ", img.shape)

print("image array = ", img)

print("pixel at index (5,5): ", img[5][5])
