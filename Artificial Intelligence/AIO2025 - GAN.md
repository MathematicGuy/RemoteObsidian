*records*: https://drive.google.com/drive/folders/1o6CIozDIbswXx3KpGaNi-a2I2C8PtoxD

### Estimate K,S,P for Conv2d
![[Pasted image 20260422165537.png]]

### How to estimate K, S, P for ConvTranpose2d (Kernel, Stride, Padding)
**Goal:** calc $H_{out}$ from $H_{in}$
**Default Formula** $$H_{out}=(H_{in}-1) \times stride-2\times padding+\text{kernel\_size}+\text{output\_padding}$$(assume dilation  = 1)

**Estimation Process**
1. *Stride* $s$ is the upsampling factor, for *2 times increase* use $stride=2$ (e.g. 32x32 to 64x64) -> *double image size*
2. *Kernel Size* $k$ usually set $kernel=2\times stride$ to fills up the missing squares and avoid checkerboard artifacts (ie. squares) ![[Pasted image 20260415155840.png | 444]] If you *add 1 kernel_size, then image upscale 1 pixel*
3. *Padding* $p$ adjust $p$ to reach the exaxt target size. you *add/remove 1 padding, image size add/reduce by 2 pixels (bc width, height combine a padding).* 

### Choosing the right activation function
Have you ever question, **why Sigmoid() and Tanh() in the last layer ?** let go through a example in GAN
Sigmoid value range $(0, 1)$ -> *map logits into probability*
Tanh value range $(-1, 1)$ -> offer better gradient flow compared to Sigmoid which can suffer from Vanishing Gradient problem. 
-> 0 hold no update information, *GAN required specific signal to for gradient update* its Generator.
-> *GAN data are normalized between $[-1, 1]$* before being fed into the network -> $Tanh$ value range is the SAME
-> both *Sigmoid and Tanh is Limited Value Range*

There Hidden and Output layer, *Hidden layer* require *Activation to activate neuron*, while *Output* layer *require Activation for specific type of problem* (classification and regression). In detail:
**1. Output Layer is problem dependent,** for
	+ *Regression* problem like predicting continous values like house price required *Acctivation with unbound output* with range $(-\infty, \infty)$ e.g. ReLU, Linear/Identity function. 
	+ *Binary Classification* (Yes/No classification) use Sigmoid (Logistic), bc its squash value between 0 and 1, representting a prob for positive/correct class.
	+ *Multi-class Classification* - use Softmax classifies One choice out of many Choice (like cat vs dog vs bird), its ensure all classes prob sum up to 1, providing a prob distribution. 
	+ *Multi-label Classification* - *each output have it own Sigmoid* (probability between 0 to 1) e.g. in 1 image classified both cat and dog.  

**2. Hidden Layers is Architecture Dependent,** these activation func introduce Non-Linearity trying to avoid vanishing gradient problem (_Non-linearity describes relationships that cannot be represented as a straight lines_-> allow model to learn/classifying multiple relationship at once)
	+ MLP and CNN: 
		ReLU - default choice due to its efficiency and speedup convergence. 
		LeakyReLU - use this if encounter Dying ReLU (dying neuron, neuron = 0) in deeper model.
	+ RNN:
		Tanh - zero centered activation function (-1, 1) -> *help optimization in sequential data.*
		Sigmoid used specifically for internal  "gates" in architecture like LSTM, GRUs. 
	+ LLM (deep network > 40 layers)
		+ SWISH and modern activation Activation func.

