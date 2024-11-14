# Core Knowledge
**Kernel**: 
+ must be positive and odd (e.g., 3, 5, 7) to have a clear center pixel.


# Basic Image Operations

**Read Image**
>loads an image from a specified file path and displays it in a window.
```python
import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)
```

**Converting Image to Greyscale**
>Converts a color image to grayscale, removing color channels and simplifying the image.
```python
# Convert to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
```

**Blurring**
>Applies a Gaussian blur to reduce image noise and detail, useful for pre-processing in edge detection.
```python
# Gaussian blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
```

**Edge Detection**
>Detects edges using the Canny edge detector, highlighting areas with significant intensity changes.
```python
# Canny edge detection
canny = cv.Canny(img, 125, 175) 
```
>`125` and `175` are the threshold values for edge detection: lower threshold and higher threshold. 
![[Pasted image 20241114141207.png]]


**Dilating & Eroding**
>Expands or shrinks edges in an image; useful for increasing or reducing detected edges or shapes.
```python
# Dilate the image
dilated = cv.dilate(canny, (7,7), iterations=3) # input image, kernel size 7x7 to apply dilation, iterations

# Erode the image
eroded = cv.erode(dilated, (3, 3), iterations=1)
```

**Resizing & Cropping**
>Changes the dimensions of the image, and cropping focuses on a specific image area.
```python
# Resize
resized = cv.resize(img, (550, 250), interpolation=cv.INTER_CUBIC)

# Crop
cropped = img[50:200, 200:400]
```

----
## Video Operations
**Reading a Video**
>Captures and displays video frames in a loop, playing until a specific key is pressed to stop.
```python
video = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = video.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
video.release()
cv.destroyAllWindows()
```

---

**Contour Detection**
>Finds contours in an image, which are useful for detecting object shapes.
```python
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) # (5, 5): width & height of the gaussian kernel
canny = cv.Canny(blur, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0,0,255), 1) # background canvas, contours, index (-1 mean apply to all), color, thickness 
```
Note: can decrease contour by blurring image
1) **Input**: must be a binary image (such as output of edge detection with Canny, where edges are white and the rest are black)  
	
2) **Retrieval Mode**: 
+  This where contour are retrieved and organized.
+ `cv.RETR_LIST`: Retrieves all contours in the image but doesn't organize them (i.e. no parent-child relationship). Each contour are independent.
+ Other `cv.RETR_`: `cv.RETR_EXTERNAL` (retrieves only outer contours), `cs.RETR_TREE` (retrieves and organizes them into a hierarchy) and `cv.RETR_CCOMP` (retrieves contours and organizes them into 2 levels: external and internal)

3) **Approximation Method**: approximate contours (note: contours are store in a contour list)
+ `cv.CHAIN_APPROX_SIMPLE`: compress horizontal and vertical and diagnol segments, only storing their enpoints. Ex: if there a line, only 2 of its endpoints get stored -> Reduces the number of points representing the contour, simplifying it without losing the shape.
+ `cv.CHAIN_APPROX_NONE`: retrieves all contour points without purely.  


**Thresholding**
> Binarizes an image by converting pixel values above or below a threshold to either black or white (i.e. 0 and 1)
> Ex: Pixels above 150 set to 1 and pixel below 255 set to 0.
```python
img = cv.imread('../Resources/Photos/cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) # input, threshold range, threshold type
```
![[Pasted image 20241114145613.png]]

```python
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

# Adaptive thresholding (input, condition_value, threshold_method, threshold_type, block_size, )
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
```
- **gray**: The grayscale image to be thresholded.
	
- **255**: The maximum value to use for thresholding. Pixels that meet the thresholding condition will be set to this value (255, in this case, for white).
	
- **cv.ADAPTIVE_THRESH_GAUSSIAN_C**: The adaptive method used to calculate the threshold value for a small region around each pixel. `GAUSSIAN_C` means it uses a Gaussian-weighted sum of the surrounding pixels.
	
- **cv.THRESH_BINARY_INV**: The type of thresholding to apply. `THRESH_BINARY_INV` inverts the output, setting pixels below the threshold to the maximum value (255) and pixels above the threshold to 0 (black).
	
- **11**: The block size, which defines the size of the neighborhood (11x11) around each pixel to calculate the threshold. This must be an odd number.
	
- **9**: The constant `C` subtracted from the calculated threshold for each neighborhood, which fine-tunes the thresholding sensitivity. A higher value of `C` makes the threshold more strict, while a lower value makes it more lenient (dễ dãi).

## Transformations
**Translation & Rotation**
>Moves an image to a new position (translation) or rotates it by a specified angle.
```python
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(img, transMat, (img.shape[1], img.shape[0]))

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    return cv.warpAffine(img, rotMat, (width, height))
```

**Resizing, Flipping, Cropping**
> Resize changes dimensions, flip mirrors the image, and crop selects an area within the image.
```python
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
flip = cv.flip(img, -1)
cropped = img[200:400, 300:400]
```

# Advance Operation
**Bitwise Operations**
>Creates composite (tổng hợp) images using bitwise operations like AND, OR, XOR, and NOT.
```python
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

bitwise_and = cv.bitwise_and(rectangle, circle)
bitwise_or = cv.bitwise_or(rectangle, circle)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
bitwise_not = cv.bitwise_not(circle)
```

**Blurring Techniques**
>Reduces image noise and smooths image detail with different blur types.
```python
average = cv.blur(img, (3,3))
gauss = cv.GaussianBlur(img, (3,3), 0)
median = cv.medianBlur(img, 3)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
```

**Color Spaces, Converting Colors**
>Converts images to various color spaces, useful for different applications.
```python
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
```

**Gradient Detection**
>Detects gradients in an image using various operators for edge enhancement.
```python
lap = cv.Laplacian(gray, cv.CV_64F)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
canny = cv.Canny(gray, 150, 175)
```
+ `cv.CV_64F`: Specifies the output image depth (64-bit floating point) to capture both positive and negative changes in gradient.
	
1. `cv.Laplacian(gray, cv.CV_64F)`: The Laplacian operator calculates the second derivative of the image, highlighting regions where the intensity changes rapidly, such as edges. This operator is especially sensitive to noise, so it’s often used on smoothed images.
	**Effect**: The result is an image where edges appear brighter against a dark background.
	
2. `cv.Sobel(gray, cv.CV_64F, 1, 0)`: The Sobel operator calculates the gradient of the image intensity, giving an approximation of the image gradient. Setting the `dx` and `dy` parameters allows control over the direction of edge detection. (x , y) 1 is x in the parameter. 
	**Effect**: Produces an image emphasizing vertical edges.
	
3. `cv.bitwise_or(sobelx, sobely)`:Combines the `sobelx` and `sobely` results to show both horizontal and vertical edges.
	**Explaination:** Using bitwise OR on `sobelx` and `sobely` highlights edges in both directions in a single image.
	
4. `cv.Canny(gray, 150, 175)`: The Canny edge detector uses a multi-stage process (gradient calculation, non-maximum suppression, and thresholding) to find strong edges and suppress noise.
	**Effect**: Provides a binary image with thin, strong edges.


**Histogram**
>Visualizes the intensity distribution of an image or specific regions.
```python
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img,mask=mask)

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()
```
Examples (only the first image reflect the code, others are for visualizing): 
![[Pasted image 20241114155808.png]]
![[Pasted image 20241114155605.png]]
![[Pasted image 20241114155622.png]]


**Masking**
>Applies a mask to focus on a specific area of interest in the image.
```python
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)     
weird_shape = cv.bitwise_and(circle, rectangle)
masked = cv.bitwise_and(img, img, mask=weird_shape)
```
Mask car photo with a circle.
![[Pasted image 20241114155448.png]]

**Rescale & Resize**
>Rescales a frame by a percentage or changes resolution in live video capture.
```python
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    return cv.resize(frame, (width, height), interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
```

**Split & Merge Channels**
>Separates or merges color channels, useful for color-specific operations.
```python
b, g, r = cv.split(img)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

merged = cv.merge([b, g, r])
```


```python

```


