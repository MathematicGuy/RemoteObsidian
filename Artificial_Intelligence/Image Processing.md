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
**Original and Scanned**
>We compare the Scanned form with the Original to check if it morph the right way.
![[Pasted image 20241205142048.png]]

### Step 2: Find keypoints in both Images
![[Pasted image 20241205142125.png]]
![[Pasted image 20241205144612.png]]
Keypoint: red-circle
+ Circle-center represent key-point location 
+ Circle-size represent key-point size
+ The radius line (i.e. line connect the center to the outside of the circle) represent key-point orientation.


### Step 3: Match keypoints in the 2 Image
![[Pasted image 20241205144640.png]]
>Matching Key Point -> Get Corresponding Keypoints
![[Pasted image 20241205144811.png]]

### Step 4: Find Homography
> Compute the homography from the set of corresponding keypoints.
![[Pasted image 20241205144921.png]]

### Step 5: Warp Image
![[Pasted image 20241205145011.png]]
![[Pasted image 20241205145033.png]]

# Module 9: Creating Panoramas using OpenCV (Skip for now)

# Module 10: High Dynamic Range (HDR) Imaging
(re-note, current note not so detail)

### Basic Idea
1. The dynamic range of images is limited to 8-bits (0 -255) per channel.
2. Very bright pixels saturate to 255
3. Very dark pixels clip to 0
### Step 1: Capture Multiple Exposures
![[Pasted image 20241205150008.png]]
![[Pasted image 20241205150043.png]]

### Step 2: Align Images
Left/Right: no HDR / with HDR (look more correct)
![[Pasted image 20241205150150.png]]
![[Pasted image 20241205150237.png]]
MTB - Median Threshold Bitmask

### Step 3: Estimate Camera Response Function
After image alignment, we need to calc camera response function
![[Pasted image 20241205150401.png]]

### Step 4: Merge Exposure into an HDR Iamge
>Note: Merging process intentionally ignore pixels values close to 0 or 255. Bc pixel values close to those extreme bring no useful information. 
![[Pasted image 20241205151638.png]]

Because ther multiple images of the scene at different exposure settings the hope is that for every pixels we have at least 1 image that contain an intensity that is neither too dark nor too bright. 

However there're 1 problem still remain which is the intensity values are no longer in the 0-255 range. Of course black can be 0, but HDR image can record light intensities from 0 to essentially infinite 
-> Need a process to bring the image intensity back down to the 0-255 range (Tonemapping)

### Step 5: Tonemapping
>Many Tonemapping algorithms are available in OpenCV. We chose Durand as it has more controls.
+ ? Mapping HDR images to 8-bits to channel images
![[Pasted image 20241205152404.png]]
Help expose to all region of the scene
![[Pasted image 20241205152445.png]]
Method 2: Tonemap using Reinhard's method
![[Pasted image 20241205152508.png]]
![[Pasted image 20241205152458.png]]
Method 3: Mantiuk's method, almost the combination of the 2 methods above.
![[Pasted image 20241205152536.png]]
![[Pasted image 20241205152609.png]]

# Module 11: Object Tracking (Important)

**Tracking:** refer to estimating the location of object and predicting its future position based on its current state and motion patterns.

**Flow:** Detect Object -> Predict object position using an  motion model (like Kalman filter or optical flow) -> fine-tune the location of the object.

### Tracker Class in OpenCV
1. BOOSTING
2. MIL
3. KCF
4. CRST
5. TLD
	Tends to recover from occulusions
6. MEDIANFLOW
	 Good for predictable slow motion
7. GOTURN
	 Deep Learning based
	 Most Accurate
8. MOSSE
	 Fastest

**Define Bounding Box and Text Annotation**
![[Pasted image 20241205155130.png]]

### Choose & Download Tracker Type 
>GOTURN for example
```python
if not os.path.isfile('goturn.prototxt') or not os.path.isfile('goturn.caffemodel'):
    print("Downloading GOTURN model zip file")
    urllib.request.urlretrieve('https://www.dropbox.com/sh/77frbrkmf9ojfm6/AACgY7-wSfj-LIyYcOgUSZ0Ua?dl=1', 'GOTURN.zip')
    
    # Uncompress the file
    !tar -xvf GOTURN.zip

    # Delete the zip file
    os.remove('GOTURN.zip')
```
![[Pasted image 20241205155845.png]]

### Create the Tracker Instance
![[Pasted image 20241205155425.png]]

### Read input video & Setup output Video
![[Pasted image 20241205155456.png]]

### Define Bounding Box
![[Pasted image 20241205155515.png]]

## Initialize Tracker
>1 Frame, 1 Bounding Box
![[Pasted image 20241205160107.png]]

### Read Frame and Track Object
![[Pasted image 20241205160124.png]]

# Module 12: Face Detection
>Can't use OpenCV to train NN, but can use it to perform inference on a pre-trained network. 