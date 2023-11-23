> AI model that generate new content from an original model
+ They **learn the underlying patterns** (mô hình cơ bản) **of the data** & use that knowledge **to create new contents.**

GAN (**Generative Adversarial Network**) contains 2 neural networks
> + **Generator & Discriminator** 
> 	creates new data instances and the discriminator evaluates them.
> + They **create a competitive setting environment** pushing datas quality, the g**enerator gets better at creating realistic data**, and the **discriminator gets better at distinguishing real from generated data**

Cách Hoạt động (Quy trình Sáng tạo và Đánh giá)
> + Generator tạo sao chép từ dữ liệu thực tế, Discriminator đánh giá sao chép dựa trên dữ liệu thực tế, nếu sao chép ko đạt thì làm lại. 
> + Khi luyện tập Generator cố gắng tạo ra bản sao chép tốt hơn để đánh lừa/qua mặt Discriminator, và Discriminator càng cải thiện khả năng nhận biết hơn.
> + Từ đó tạo ra các hình ảnh với độ chân thực cao.
1. **Generator:**
    
    - The generator starts with random noise and generates images.
    - Initially, these generated images might look like random noise.
2. **Discriminator:**
    
    - The discriminator is presented with both real and generated images.
    - It learns to distinguish between real and generated images.
3. **Training:**
    
    - The generator and discriminator are trained iteratively.
    - The generator tries to create more realistic images to fool the discriminator.
    - The discriminator gets better at distinguishing between real and generated images.
4. **Convergence (hội tụ):** 
    
    - Over time, the generator becomes adept at creating realistic images.
    - The discriminator becomes skilled at telling the difference between real and generated images.
5. **Generation:**
    
    - The trained generator can then be used to create entirely new images that resemble the training data.
**Real-World Example:**
		Deepfake videos. Use GAN to manipulate and generate highly realistic videos by swapping faces or altering the content of existing videos. 
