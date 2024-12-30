+ ! remember to filter NULL
**references:**
+ [invoice information extraction](https://medium.com/analytics-vidhya/invoice-information-extraction-using-ocr-and-deep-learning-b79464f54d69)
+ [id card infor extraction website](https://github.com/liemkg1234/WebOCR_identitycard?tab=readme-ov-file)
+ [image alignment guide](https://viblo.asia/p/pytorch-tutorial-3-alignment-anh-chung-minh-thu-voi-pytorch-huong-dan-de-nhu-an-keo-4dbZNJ8mZYM) 
+ [image detection using tensorflow v2 api](https://viblo.asia/p/chinh-phuc-bai-toan-object-detection-voi-tensorflow-v2-api-trong-5-phut-1VgZvMRrKAw)

![[Pasted image 20241212142019.png]]
Later: 
Improve Model prediction with different lighting (Augment in Roboflow, minimize manual labeling by choosing 4-5 different diff lighting condition then augment them to simulate more lighting condition)
+ Apply NMS later
+ Add Earepisodely Stopping
+ Gather a lot of image for auto labeling using pre-trained model  -> add this dataset with label to the processed main dataset (in my pre-processing lab)
+ Test and Detect Text Clarity
+ Compare current image pre-processing method with canny (How to reduce the vietname circle crest behind the text)
+ Summarize data using Summarization Model.  

Plan: 


Train New YOLO Model with Greyscale pre-processing
Load New Model to my Detection Anomaly and Modify it into ID Card Detection Project

Test: 
Initialize Perspective Transform
Train Text Detection Model (VietOCR)




---

**Run Detection Model**
```python
import cv2
from ultralytics import YOLOv10

# Load the YOLOv10 model
model = YOLOv10(f'{HOME}/weights/yolov10n.pt')

# Open a connection to the webcam (0 for the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform inference on the current frame
    results = model(source=frame, conf=0.25)
    
    # Render the results on the frame
    frame_with_results = results.render()[0]
    
    # Display the frame with detections
    cv2.imshow('YOLOv10 Live Detection', frame_with_results)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

```

**Return Detection Result in dictionary format**
```python
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    """
    Perform object detection on an uploaded image with preprocessing.
    """
    try:
        # Load the uploaded image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_np = np.array(image)[:, :, ::-1]  # Convert PIL image to BGR NumPy array

        # Preprocess the image (including resizing)
        preprocessed_image = preprocess_frame(image_np)
        
        # Perform object detection with YOLO
        results = model(preprocessed_image, conf=0.4)

        # Process results
        detections = []
        for result in results:
            for box in result.boxes:
                bbox = box.xyxy.tolist()[0]  # Bounding box coordinates [x1, y1, x2, y2]
                confidence = box.conf.tolist()[0]  # Confidence score
                class_id = int(box.cls.tolist()[0])  # Class ID
                detections.append({
                    "class_id": config['names'][class_id],
                    "confidence": confidence,
                    "bbox": bbox
                })

        # Annotate the image with bounding boxes
        annotated_image = annotate_image(preprocessed_image, detections)

        # Save the annotated image to a file
        original_filename = file.filename
        save_filename = f"processed_{os.path.splitext(original_filename)[0]}.jpg"
        save_path = os.path.join("validation/output", save_filename)
        cv2.imwrite(save_path, annotated_image)
        
        # Optionally, return the file path or a URL for the saved image
        return JSONResponse(content={"detections": detections, "image_path": save_path})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
```

---

### Vocabularies
FLOPs: Floating Point Operations per Second. 
+ Floating Point mean doing calculation involving fractions or decimal
+ FLOPs count how many of these decimal-based calculations a computer or model can do in a second.

**Examples:**
+ Small FLOPs (Simple Model): If a model uses fewer FLOPs, it might process an image quickly but with less accuracy. Imagine spotting apples in a basket but missing the oranges because you're in a hurry.
	
+ Large FLOPs (Complex Model): If a model uses many FLOPs, it works more thoroughly. This is like carefully inspecting the basket and identifying every single fruit but taking more time.

Compare YOLO11s vs YOLO11n: [[YOLO Models performance comparison]]
Winner: YOLO11n -> Better without lossing much accuracy

---
(Understand disk footprint later)
 `footprint=disk(15)` with a radius of 15 pixels. This footprint is then used by the `rank.equalize` function to perform local histogram equalization on the image.
 + `disk(15):` create a disk-shaped structureing element with radius of 15.
 + `disk`: fuction genarates a 2D array where element within the specified radius (i.e. 15) are set to 1, and elements outside to 0.
+  **Used**: by the `rank.equalize` function to define the neighborhood around each pixel for local histogram equalization.
	![[Pasted image 20241212110144.png]]


# Problems: 

### Skews Parallelogram when Reconstructing using midpoint

**Reasons for Out-of-Bounds Coordinates:**
1. **Inaccurate Input Coordinates:** The most likely reason is that the initially detected corners (botleft, botright, topleft in your example) are not perfectly accurate. Even small errors in the positions of the detected corners can be amplified when calculating the missing corner, especially if the ID card is significantly skewed or distorted.
    
    - **Object Detection Errors:** The underlying object detection model might be:
        
        - **Misidentifying corners:** It might be selecting points that aren't true corners of the ID card.
            
        - **Imprecise localization:** Even if it correctly identifies the corner, the bounding box might not be perfectly tight, leading to slightly offset coordinates.
            
        - **Confused by background clutter or noise:** If the image background is complex, the detector might be confused.
            
2. **Perspective Distortion:** Real-world images of ID cards often suffer from perspective distortion. Your calculate_missed_coord_corner function assumes the ID card is a perfect parallelogram. When perspective is present, the four corners will not form a perfect parallelogram, and using the midpoint-based reconstruction can lead to inaccurate and out-of-bounds results. In your specific case:
    
    - If the top of the ID card is further away from the camera than the bottom, the topright corner will appear closer to the topleft and potentially higher up (smaller y-value). Your calculation, assuming a parallelogram, tries to extend the top edge horizontally, resulting in a negative y-value.
        
3. **Edge Cases and Extreme Skew:** If the ID card is extremely rotated or skewed in the image, the parallelogram assumption breaks down even further. The two provided corners might not accurately define the orientation and size of the card's edges for a reliable parallelogram completion.
    
4. **Numerical Precision:** While less likely in this specific scenario with floats, sometimes minor numerical precision issues can accumulate. However, the magnitude of your offset suggests a more fundamental problem.

### Solutions
1) **Improve Corner Detection:** The most impactful solution is to improve the accuracy of your initial corner detection. This involves:

2) - **Constrain the Output:** After calculating the missing corner, explicitly check if the coordinates fall within the image boundaries (0 to width, 0 to height). If they don't, you can implement strategies like:
    
    - **Clamping:** Set the out-of-bounds coordinate to the nearest boundary value (e.g., if y < 0, set y = 0). This is a simple but potentially inaccurate fix.
        
    - **Flagging and Ignoring:** If a coordinate is out of bounds, you can flag the reconstruction as potentially unreliable and skip further processing for that image or use a fallback method.

3) **Account for Perspective Distortion:** More sophisticated methods can account for perspective:
    
    - **Homography Estimation:** If you have four reasonably accurate corner detections (or can reliably estimate three and have a good prior), you can estimate a homography matrix. This matrix describes the transformation between the distorted quadrilateral in the image and a rectangular template. This is a more accurate approach than assuming a parallelogram.
        
    - **Perspective Correction Techniques:** Apply image transformations to "unwarp" the ID card before or after corner detection. This requires identifying a plane in the image.

4) **Validate Input Corners:** Before calculating the missing corner, perform some basic validation checks on the input corners:
    
    - **Check for reasonable ordering:** For example, topleft's x-coordinate should generally be less than topright's x-coordinate. Similarly, y-coordinates should follow a general pattern.
        
    - **Check for proximity:** The distances between the provided corners should be within a reasonable range based on the expected size of an ID card. Large discrepancies might indicate errors.


![[Pasted image 20241229153423.png]]


Tôi muốn bạn tóm tắt đoạn latex trên bằng format dưới đây cho {topic} ở trên

Format báo cáo dự án:
\subsection{Phương pháp thực hiện}
\subsubsection{Mô tả phương pháp thực hiện}
\subsubsection{Quy trình thực hiện}
\subsection{Kết quả đạt được}
\subsection{Khó khăn và cách khắc phục}
\subsubsection{Khó khăn gặp phải}
\subsubsection{Cách khắc phục}


**BCE and KL Divergence**
```
\paragraph{Kullback-Leibler (KL) Divergence}
\begin{itemize}
    \item \textbf{Định nghĩa trực quan:} Đo sự khác biệt giữa hai phân phối xác suất.
     \item \textbf{Công thức (cho phân phối rời rạc):}
        $$D_{KL}(P||Q) = \sum_{x} P(x) \log \left( \frac{P(x)}{Q(x)} \right)$$
    \item \textbf{Ví dụ trực quan:} Nếu KL Divergence giữa hai phân phối là 0, nghĩa là hai phân phối này giống hệt nhau.
    \item \textbf{Ứng dụng:}
        \begin{itemize}
             \item Đo sự khác biệt giữa phân phối xác suất dự đoán và phân phối xác suất thực tế trong mô hình xác suất.
             \item Trong Variational Autoencoders (VAEs) và Generative Adversarial Networks (GANs).
            \item Trong Natural Language Processing (NLP) để so sánh phân phối từ của các văn bản.
        \end{itemize}
    \item \textbf{Ưu điểm:}
        \begin{itemize}
            \item Đo lường sự khác biệt giữa các phân phối, không chỉ đơn thuần là sai số.
            \item Phù hợp với các mô hình xác suất.
        \end{itemize}
    \item \textbf{Nhược điểm:}
        \begin{itemize}
             \item Không đối xứng: KL(P||Q) ≠ KL(Q||P).
             \item Không xác định nếu có giá trị bằng 0 trong phân phối thực tế.
        \end{itemize}
\end{itemize}
\paragraph{Binary Cross-Entropy (BCE)}
\begin{itemize}
    \item \textbf{Định nghĩa trực quan:} Đo sự khác biệt giữa hai phân phối xác suất nhị phân.
      \item \textbf{Công thức:}
          $$BCE = -\frac{1}{n} \sum_{i=1}^n [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]$$
    \item \textbf{Ví dụ trực quan:} Giá trị BCE càng nhỏ, mô hình càng dự đoán tốt các nhãn nhị phân.
    \item \textbf{Ứng dụng:}
        \begin{itemize}
             \item Hàm mất mát trong bài toán phân loại nhị phân.
             \item Huấn luyện các mô hình neural network với lớp đầu ra sigmoid.
        \end{itemize}
    \item \textbf{Ưu điểm:}
        \begin{itemize}
            \item Phù hợp với bài toán phân loại nhị phân.
            \item Tính được gradient, giúp mô hình học nhanh hơn.
        \end{itemize}
    \item \textbf{Nhược điểm:} Chỉ áp dụng cho bài toán nhị phân.
\end{itemize}
```

calculus2.tex
```
\section{Mạng Neural và Backpropagation}

\subsection{Phương pháp thực hiện}
\subsubsection{Mô tả mô hình mạng Neural}
Mô hình mạng Neural được sử dụng trong bài toán phân loại này có cấu trúc hai lớp:
\begin{itemize}
    \item Lớp đầu vào (Input Layer): $n_x = 2$ (các đặc trưng $x_1, x_2$).
    \item Lớp ẩn (Hidden Layer): $n_h = 2$ (hai nơ-ron ở lớp ẩn).
    \item Lớp đầu ra (Output Layer): $n_y = 1$ (giá trị dự đoán $\hat{y}$).
    \begin{figure}[h!]
    \centering
    \includegraphics[width=1\linewidth]{images/nn_model_2_layers} % Replace 'filename' with your image file's name without extension
    \caption{Neural Network Model 2 Layers}
    \label{fig:your-label}
\end{figure}
\end{itemize}
Các công thức toán học cho quá trình lan truyền tiến được mô tả như sau:
\begin{align*}
    Z^{[1]} &= W^{[1]} X + b^{[1]}, \\
    A^{[1]} &= \sigma\left(Z^{[1]}\right), \\
    Z^{[2]} &= W^{[2]} A^{[1]} + b^{[2]}, \\
    \hat{Y} &= A^{[2]} = \sigma\left(Z^{[2]}\right),
\end{align*}
trong đó:
\begin{itemize}
    \item $W^{[1]}, b^{[1]}$: trọng số và độ lệch lớp ẩn.
    \item $W^{[2]}, b^{[2]}$: trọng số và độ lệch lớp đầu ra.
    \item $\sigma(x) = \frac{1}{1 + e^{-x}}$: hàm kích hoạt sigmoid.
\end{itemize}

\subsubsection{Quy trình thực hiện}


\textbf{A.  Single Training Examples}

\begin{enumerate}
    \item \textbf{Khởi tạo tham số:} Giống như trường hợp Single Training Example.
s
    \item \textbf{Lan truyền tiến (Forward Propagation):}
    \begin{itemize}
        \item Xây dựng ma trận đầu vào $X$ (kích thước $(n_x, m)$) và vector nhãn $Y$ (kích thước $(n_y, m)$), trong đó $m$ là số lượng ví dụ huấn luyện.
        \item Tính toán đầu ra trước khi kích hoạt của lớp ẩn:
        $$Z^{[1]} = W^{[1]} X + b^{[1]}$$
        trong đó $b^{[1]}$ được broadcast thành ma trận có kích thước $(n_h, m)$.
        \item Áp dụng hàm kích hoạt sigmoid cho lớp ẩn:
        $$A^{[1]} = \sigma\left(Z^{[1]}\right)$$
        \item Tính toán đầu ra trước khi kích hoạt của lớp đầu ra:
        $$Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]}$$
        trong đó $b^{[2]}$ được broadcast thành vector có kích thước $(n_y, m)$.
        \item Áp dụng hàm kích hoạt sigmoid cho lớp đầu ra để có xác suất dự đoán:
        $$A^{[2]} = \sigma\left(Z^{[2]}\right)$$
        \item Dự đoán nhãn $\hat{Y}$:
        $$\hat{Y} = \begin{cases} 1 & \mbox{if } A^{[2]} > 0.5, \\ 0 & \mbox{otherwise }. \end{cases}$$
    \end{itemize}

    \item \textbf{Hàm mất mát (Cost Function):}
    \begin{itemize}
        \item Sử dụng hàm Binary Cross-Entropy:
        $$J = -\frac{1}{m} \sum_{i=1}^m \left[ y^{(i)} \log(\hat{y}^{(i)}) + (1 - y^{(i)}) \log(1 - \hat{y}^{(i)}) \right]$$
    \end{itemize}

    \item \textbf{Lan truyền ngược (Backward Propagation):}
    \begin{itemize}
        \item Tính đạo hàm riêng của hàm mất mát theo các tham số:
        \begin{align*}
            \frac{\partial J}{\partial W^{[2]}} &= \frac{1}{m}\left(A^{[2]}-Y\right)\left(A^{[1]}\right)^T,\\
            \frac{\partial J}{\partial b^{[2]}} &= \frac{1}{m} \sum_{i=1}^m \left(A^{[2]} - Y\right),\\
            \frac{\partial J}{\partial W^{[1]}} &= \frac{1}{m}\left(\left(W^{[2]}\right)^T \left(A^{[2]} - Y\right)\cdot \left(A^{[1]}\cdot\left(1-A^{[1]}\right)\right)\right)X^T,\\
            \frac{\partial J}{\partial b^{[1]}} &= \frac{1}{m} \sum_{i=1}^m \left(\left(W^{[2]}\right)^T \left(A^{[2]} - Y\right)\cdot \left(A^{[1]}\cdot\left(1-A^{[1]}\right)\right)\right),
        \end{align*}
        trong đó "$\cdot$" ký hiệu phép nhân element-wise.
    \end{itemize}

    \item \textbf{Cập nhật tham số (Gradient Descent):}
    \begin{itemize}
        \item Sử dụng learning rate $\alpha$ để cập nhật tham số:
        \begin{align*}
            W^{[1]} &:= W^{[1]} - \alpha \frac{\partial J}{\partial W^{[1]}}, \\
            b^{[1]} &:= b^{[1]} - \alpha \frac{\partial J}{\partial b^{[1]}}, \\
            W^{[2]} &:= W^{[2]} - \alpha \frac{\partial J}{\partial W^{[2]}}, \\
            b^{[2]} &:= b^{[2]} - \alpha \frac{\partial J}{\partial b^{[2]}}.
        \end{align*}
    \end{itemize}
    \item Lặp lại các bước 2-5 cho đến khi hội tụ hoặc đạt được số epoch tối đa.
\end{enumerate}


\textbf{B. Multiple Training Example}

\begin{enumerate}
    \item \textbf{Khởi tạo tham số:}
    \begin{itemize}
        \item $W^{[1]}$: Ma trận trọng số lớp ẩn, kích thước $(n_h, n_x) = (2, 2)$. Khởi tạo ngẫu nhiên các giá trị nhỏ.
        \item $b^{[1]}$: Vector độ lệch lớp ẩn, kích thước $(n_h, 1) = (2, 1)$. Khởi tạo bằng 0.
        \item $W^{[2]}$: Vector trọng số lớp đầu ra, kích thước $(n_y, n_h) = (1, 2)$. Khởi tạo ngẫu nhiên các giá trị nhỏ.
        \item $b^{[2]}$: Độ lệch lớp đầu ra, là một số vô hướng. Khởi tạo bằng 0.
    \end{itemize}

    \item \textbf{Lan truyền tiến (Forward Propagation):}
    \begin{itemize}
        \item Với mỗi ví dụ huấn luyện $x^{(i)} = \begin{bmatrix} x_1^{(i)} \\ x_2^{(i)} \end{bmatrix}$:
        \item Tính toán đầu ra trước khi kích hoạt của lớp ẩn:
        \begin{align*}
            z_1^{[1](i)} &= w_{1,1}^{[1]} x_1^{(i)} + w_{2,1}^{[1]} x_2^{(i)} + b_1^{[1]} = W_1^{[1]}x^{(i)} + b_1^{[1]},\\
            z_2^{[1](i)} &= w_{1,2}^{[1]} x_1^{(i)} + w_{2,2}^{[1]} x_2^{(i)} + b_2^{[1]} = W_2^{[1]}x^{(i)} + b_2^{[1]}.
        \end{align*}
        \item Viết gọn lại dưới dạng vector:
        $$z^{[1](i)} = W^{[1]} x^{(i)} + b^{[1]} = \begin{bmatrix}z_1^{[1](i)} \\ z_2^{[1](i)}\end{bmatrix}$$
        \item Áp dụng hàm kích hoạt sigmoid cho lớp ẩn:
        $$a^{[1](i)} = \sigma\left(z^{[1](i)}\right) = \begin{bmatrix}\sigma\left(z_1^{[1](i)}\right) \\ \sigma\left(z_2^{[1](i)}\right)\end{bmatrix}$$
        \item Tính toán đầu ra trước khi kích hoạt của lớp đầu ra:
        $$z^{[2](i)} = w_1^{[2]} a_1^{[1](i)} + w_2^{[2]} a_2^{[1](i)} + b^{[2]}= W^{[2]} a^{[1](i)} + b^{[2]}$$
        \item Áp dụng hàm kích hoạt sigmoid cho lớp đầu ra để có xác suất dự đoán:
        $$a^{[2](i)} = \sigma\left(z^{[2](i)}\right)$$
        \item Dự đoán nhãn:
        $$\hat{y}^{(i)} = \begin{cases} 1 & \mbox{if } a^{[2](i)} > 0.5, \\ 0 & \mbox{otherwise }. \end{cases}$$
    \end{itemize}

    \item \textbf{Hàm mất mát (Cost Function):}
    \begin{itemize}
        \item Sử dụng hàm Binary Cross-Entropy:
        $$L(a^{[2](i)}, y^{(i)}) = - y^{(i)} \log(a^{[2](i)}) - (1-y^{(i)}) \log(1- a^{[2](i)})$$
        \item Tính trung bình cộng của hàm mất mát trên toàn bộ tập huấn luyện (ở đây chỉ xét 1 ví dụ):
        $$J(W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}) = L(a^{[2](i)}, y^{(i)})$$
    \end{itemize}

    \item \textbf{Lan truyền ngược (Backward Propagation):}
    \begin{itemize}
        \item Tính đạo hàm riêng của hàm mất mát theo các tham số:
        \begin{align*}
            \frac{\partial J}{\partial W^{[2]}} &= \left(a^{[2](i)} - y^{(i)}\right) {a^{[1](i)}}^T,\\
            \frac{\partial J}{\partial b^{[2]}} &= \left(a^{[2](i)} - y^{(i)}\right),\\
            \frac{\partial J}{\partial W^{[1]}} &= \begin{bmatrix}
            \frac{\partial J}{\partial w_{1,1}^{[1]}} & \frac{\partial J}{\partial w_{2,1}^{[1]}} \\
            \frac{\partial J}{\partial w_{1,2}^{[1]}} & \frac{\partial J}{\partial w_{2,2}^{[1]}} \end{bmatrix} = \begin{bmatrix}
            \left(a^{[2](i)} - y^{(i)}\right) w_1^{[2]} \left(a_1^{[1](i)}\left(1 - a_1^{[1](i)}\right)\right) x_1^{(i)} &
            \left(a^{[2](i)} - y^{(i)}\right) w_1^{[2]} \left(a_1^{[1](i)}\left(1-a_1^{[1](i)}\right)\right) x_2^{(i)}  \\
            \left(a^{[2](i)} - y^{(i)}\right) w_2^{[2]} \left(a_2^{[1](i)}\left(1-a_2^{[1](i)}\right)\right) x_1^{(i)} &
            \left(a^{[2](i)} - y^{(i)}\right) w_2^{[2]} \left(a_2^{[1](i)}\left(1-a_2^{[1](i)}\right)\right) x_2^{(i)}\end{bmatrix},\\
            \frac{\partial J}{\partial b^{[1]}} &= \begin{bmatrix}
            \left(a^{[2](i)} - y^{(i)}\right) w_1^{[2]} \left(a_1^{[1](i)}\left(1 - a_1^{[1](i)}\right)\right) \\
            \left(a^{[2](i)} - y^{(i)}\right) w_2^{[2]} \left(a_2^{[1](i)}\left(1-a_2^{[1](i)}\right)\right)
            \end{bmatrix}.
        \end{align*}
    \end{itemize}

    \item \textbf{Cập nhật tham số (Gradient Descent):}
    \begin{itemize}
        \item Sử dụng learning rate $\alpha$ để cập nhật tham số:
        \begin{align*}
            W^{[1]} &:= W^{[1]} - \alpha \frac{\partial J}{\partial W^{[1]}}, \\
            b^{[1]} &:= b^{[1]} - \alpha \frac{\partial J}{\partial b^{[1]}}, \\
            W^{[2]} &:= W^{[2]} - \alpha \frac{\partial J}{\partial W^{[2]}}, \\
            b^{[2]} &:= b^{[2]} - \alpha \frac{\partial J}{\partial b^{[2]}}.
        \end{align*}
    \end{itemize}
    \item Lặp lại các bước 2-5 cho đến khi hội tụ.
\end{enumerate}
```