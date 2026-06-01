14x14x3x2 
2 for repeat 
[1,16,28] - [1, w, h]
grid_thw - cái wxh patch đc flatten

group 3 patchs into a sequence 


hidden_states -> CNN CONV 3D layer -> feature_map [448, 1280]
What made OCR good -> rotery_position_embedding (RoPE) 
rotate 2 adj vector - like PE of transformer but its rotate after that.  
x1, x2 pixel cooordinate.  cos & sin like transformer's PE 
![[Pasted image 20251031155037.png]]
After RoPE -> Value close to eachother. Relative position 
-> relative position - position within a Patch. 
Window_index - extract local features using a window size WxH.

mRoPE - rotate image token, video token, text token.
-> Absolute Position -> position of each frames within the video. -> spatial & temporal information 
![[Pasted image 20251031155907.png]]


Phuong Insight - how to read research English paper !
AI Engineer vs AI Researcher 
Conference - search CVF, Google Scholar
Bắt đầu từ bài review/summarize -> original paper. 


