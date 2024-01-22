import cv2
import numpy as np
import math
import keyboard as k
from tkinter import filedialog

img = filedialog.askopenfilename()

error = None
slope_weight = 30
dist_weight = 0.8


#Mask
def poly_image(image):
   h,w = image.shape[:2]
   poly = np.array([[(0,h-math.floor(h*0.1)),(0, h), (w, h), (w,h-math.floor(h*0.1)),(math.floor(w/2+(w*0.08)), math.floor(h*0.55)), (math.floor(w/2-(w*0.08)), math.floor(h*0.55))]])
   copy = image.copy()
   cv2.fillPoly(copy, poly, color=(0, 255, 0))
   return cv2.addWeighted(image, 0.85, copy, 0.15, 0)

#Gray color filter
def gray(image):
  image=np.asarray(image)
  return cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#Gaussian blur to reduce noise and smoothen the image
def gauss(image):
  return cv2.GaussianBlur(image,(5,5),0)

#Canny edge detection
def canny(image):
    edges = cv2.Canny(image,50,150)
    return edges

#Area of interest (detect filter lanes)
def area_of_interest(image):
   h, w = image.shape[:2]
   triangle = np.array([[(0,h-math.floor(h*0.1)),(0, h), (w, h), (w,h-math.floor(h*0.1)),(math.floor(w/2+(w*0.08)), math.floor(h*0.55)), (math.floor(w/2-(w*0.08)), math.floor(h*0.55))]])
   mask = np.zeros_like(image)
   cv2.fillPoly(mask, triangle, 255)
   masked_image = cv2.bitwise_and(image, mask)
   return masked_image

#Display lines
def display_lines(image, lines, color=(255,0,0)):
   line_image = np.zeros_like(image)
   if lines is not None:
      for line in lines:
         x1,y1,x2,y2 = line.reshape(4)
         cv2.line(line_image,(x1,y1),(x2,y2),color,10)
   return line_image

#Line optimisation
def average_slope_intercept(image,lines):
   leftFit= []
   rightFit = []
   for line in lines:
      x1, y1, x2, y2 = line.reshape(4)
      parameters = np.polyfit((x1,x2),(y1,y2), 1)
      slope = parameters[0]
      intercept = parameters[1]
      if slope < 0:
         leftFit.append((slope, intercept))
      else:
         rightFit.append((slope, intercept))
   leftFitAVG = np.average(leftFit, axis=0)
   rightFitAVG = np.average(rightFit, axis=0)
   try:
    leftLine = make_coords(image, leftFitAVG)
   except: pass
   try:
    rightLine = make_coords(image, rightFitAVG)
   except: pass
   return np.array([leftLine, rightLine])
def make_coords(image, line_parameters):
   try:
      slope, intercept = line_parameters  
      y1 = image.shape[0]
      y2 = int(y1*(3/5))
      x1 = int((y1-intercept)/slope)
      x2 = int((y2-intercept)/slope)
      return np.array([x1,y1,x2,y2])
   except:
      return

#Center line
def center_line(image, averaged_lines):
   left, right = averaged_lines
   lx1, y1, lx2, y2 = left.reshape(4)
   rx1, y1, rx2, y2 = right.reshape(4)
   x1 = math.floor((rx1+lx1) / 2)
   x2 = math.floor((rx2+lx2) / 2) 
   line = np.array([x1,y1,x2,y2])
   return line

#Calculate error
def get_error(image, line):
   try:
      _, w = image.shape[:2]
      x1, y1, x2, y2 = line.reshape(4)
      m = (y2-y1)/(x2-x1)
      dist = w/2 - x1
      slope_error = (1/m)*slope_weight
      dist_error = dist*dist_weight
      return slope_error + dist_error
   except:
      return 0
   
frame = cv2.imread(img)
#print(frame)

poly_img = poly_image(frame)

canny_image = canny(gauss(gray(frame)))
cropped = area_of_interest(canny_image)
lines = cv2.HoughLinesP(cropped,2,np.pi/180,80,np.array([]),minLineLength=40,maxLineGap=5)
averaged_lines = average_slope_intercept(frame, lines)
center = center_line(frame, averaged_lines)
center_image = display_lines(frame, [center], (0,200,255))
error = get_error(frame, center)
line_image = display_lines(frame, averaged_lines)
combination = cv2.addWeighted(poly_img, 1, line_image, 1, 0)
combination2 = cv2.addWeighted(combination, 1, center_image, 0.5, 0)

cv2.imshow("result", combination2)
if cv2.waitKey(0) == ord("s"):
   f = filedialog.asksaveasfile(mode='w', defaultextension=".jpg", filetypes=[("All files", "*.*"), ("Image files", (".png", ".jpg", ".jpeg"))] )
   if f: cv2.imwrite(f.name, combination2)