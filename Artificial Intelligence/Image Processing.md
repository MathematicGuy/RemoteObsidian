[source](https://www.youtube.com/watch?v=P4Z8_qe2Cu0&t=2202s) 
# Module 1: Getting Started
+ ! `[0, 255] <-> [Black, White]`
**Import Library and Display image by NxN pixel**
![[Pasted image 20241205101143.png]]


**Display Images using Matplotlib**
Color Map by Default
![[Pasted image 20241205101240.png]]
Colormap = 'gray'
![[Pasted image 20241205101317.png]]
Read Image as Gray Scale, quite cool huh
![[Pasted image 20241205101356.png]]
![[Pasted image 20241205101415.png]]

Opencv use BGR. So RGB image get mapped to BGR
![[Pasted image 20241205101653.png]]
>Keep in mind that OpenCV store image in BGR.
![[Pasted image 20241205101724.png]]

**Extract Specific color from a Image**
![[Pasted image 20241205102101.png]]

### Converting to different Color Spaces
![[Pasted image 20241205102144.png]]
Ex: RGB to RGB, or RBG to GRAYSCALE
![[Pasted image 20241205102218.png]]
Ex2: Change to HSV (Hue, Staturation, Value) color space
+ *Hue:* Original/Pure Color, *Staturation:* color intensity, *Value:* lightness or darkness of a color. By Adjust S and V we can create many more color.
![[Pasted image 20241205102326.png]]

### Modifying Individual Channel
> Modifying Hue color channel and convert image's color space back to RGB.
![[Pasted image 20241205103045.png]]

### Saving Image
>Like `imread()` for saving file
![[Pasted image 20241205103159.png]]

# Module 2: Basic Image Manipulation

### Crop Image 
>Extract Image Region
![[Pasted image 20241205103651.png]]

### Resizing Images
![[Pasted image 20241205103348.png]]

**Specifying exact size of the image**
![[Pasted image 20241205103513.png]]

**Resize while maintaining aspect ratio**
![[Pasted image 20241205103553.png]]

# Module 3: Image Annotation
>**Includes**: Draw lines, Draw circles, Draw rectangles, Add text
### Drawing a Line
![[Pasted image 20241205103932.png]]
![[Pasted image 20241205103945.png]]

### Drawing a Circle
![[Pasted image 20241205104014.png]]
![[Pasted image 20241205104030.png]]

### Draw Rectangle
![[Pasted image 20241205104047.png]]
**pt1:** upper left point
**pt2:** lower right point
![[Pasted image 20241205104056.png]]

### Adding Text
![[Pasted image 20241205104157.png]]
![[Pasted image 20241205104235.png]]
 
# Module 4: Image Enhancement 
### Adjust Brightness
Method: Create a matrix the same size as the image, multiply it with a factor and add matrix value to the image.   
![[Pasted image 20241205093047.png]]

### Multiplication or Constract
+ @ Contrast is the difference in the intensity value of the pixels of an image.
**Method:** Just like adding a matrix can change the brightness of the image. Multiplying matrix with image's pixels value can improve the constract of the image.
+ ? **Problems:** when mulitiplying, some pixels value exceed 255 and restart itself  to 1 (+ matrix value) 
![[Pasted image 20241205093322.png]]

**Handling Overflow using `np.clip`**
>Clip value in the range between `[0, 255]`
![[Pasted image 20241205094230.png]]

### Image Thresholding
> Image's pixels value > threshold become 1 else 0. Basically Binarified the whole image by a threshold.
>![[Pasted image 20241205094523.png]]![[Pasted image 20241205094538.png]]
>Example: ![[Pasted image 20241205094617.png]]
>**More Discrete Example**: Highlight Music Sheet  by threshold:
>+ **50 Problem:** Too Low, can't even catch black music note in bright light  
![[Pasted image 20241205094726.png]]
>+ **130 Problem:** Too High, any part with shadow get blacken out
>+ **Thresholded (adaptive):** balance 
![[Pasted image 20241205095006.png]] 

### Bitwise Operations
![[Pasted image 20241205095426.png]]

**Bitwise AND Operator**
![[Pasted image 20241205095515.png]]

**Bitwise OR Operator**
![[Pasted image 20241205095529.png]]

**Bitwise XOR Operator**
![[Pasted image 20241205095557.png]]

**Application: Logo Manipulation**
![[Pasted image 20241205095757.png]]
**Step 1:** Read Foreground Image
![[Pasted image 20241205095820.png]]
**Step 2:** Read Background Image
![[Pasted image 20241205095844.png]]
**Step 3:** Create Inverse Mask of your Choice
**Create Mask for original Image:** grayscale image by apply thresholding
![[Pasted image 20241205095857.png]]
**Invert the Mask**
![[Pasted image 20241205095934.png]]
**Step 4: Apply background on the Mask:** Combine background image with cocacola image on *img_mask* area (i.e. white pixels areas)  
![[Pasted image 20241205100114.png]]

**Isolate foreground from Image**
![[Pasted image 20241205100517.png]]

**Result: Merge Foreground and Background**
![[Pasted image 20241205100813.png]]

# Module 5: Accessing the Camera
> Important

![[Pasted image 20241205112203.png]]
Source s = 0 mean access the web cam. 
`sys.argv[1]` access the 2nd camara from your system if existed
![[Pasted image 20241205112253.png]]
**Read frame and frame condition (True or False)** from the video source
![[Pasted image 20241205112412.png]]
And show the frame
![[Pasted image 20241205112456.png]]

### Read Video from Source
>read video and check if it was succesfully
![[Pasted image 20241205112659.png]]

**Read and display one frame** ![[Pasted image 20241205112748.png]]


### Write Video in OpenCV
![[Pasted image 20241205112845.png]]
![[Pasted image 20241205113035.png]]

**Read frames and write to file**
>**code description:** read frame and if there still frame left in video then write frame
>![[Pasted image 20241205113128.png]]![[Pasted image 20241205113151.png]]

# Module 7: Image Filtering and Edge Detection

```python
feature_params = dict(maxCorners = 500, qualityLevel = 0.2, minDistance = 15, blockSize = 9)
```
1. `maxCorners = 500`
+ Specifies the maximum number of corners to return.
+ If more than 500 corners are found, only the 500 strongest ones will be retained.

2. `qualityLevel = 0.2`
+ Represents the minimal accepted quality of image corners.
+ A corner’s quality is calculated relative to the best corner, which is assigned a value of 1.0. Relativ to the best corner mean: 
	$Threshold = \text{qualityLevel} \times  \text{Best coner value}$
	Only satify corners retain: $$R \geq \text{qualityLevel} \times R_{max}$$+ A `qualityLevel` of `0.2` means that corners below 20% of the maximum corner quality will be rejected.

3. `minDistance = 15`
- The minimum Euclidean distance (in pixels) between detected corners.
- This helps avoid detecting corners that are too close to each other.

4. **`blockSize = 9`**
- The size of the neighborhood (in pixels) used for corner detection.
- A larger block size smooths the image more and results in fewer but more robust corners.

# Module 8: Image Features and Image Alignment 

**Morphing Image**: by detection 4 corners point then morp 
![[Pasted image 20241205141826.png]]

### Step 1: Read Template and Scanned Iamge
![[Pasted image 20241205142003.png]]
![[Pasted image 20241205142035.png]]
**After and Before**
![[Pasted image 20241205142048.png]]

### Step 2: Find keypoints in both Images
![[Pasted image 20241205142125.png]]

