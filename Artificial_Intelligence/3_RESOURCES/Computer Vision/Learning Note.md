---
category: "3_RESOURCES/Computer Vision/Learning Note.md"
summary: "### Building Machine Learning model by Quantifying Uncertainty model
Try to prove: $$[f^{-1}]'(x)=\frac{1}{f'(f^{-1}(x))}$$

Start with the definition of the inverse
$$f(f^{-1}(x))=x$$
Take the der..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.111670+00:00"
---
### Building Machine Learning model by Quantifying Uncertainty model
Try to prove: $$[f^{-1}]'(x)=\frac{1}{f'(f^{-1}(x))}$$

Start with the definition of the inverse
$$f(f^{-1}(x))=x$$
Take the derivative of both sides
$$\frac{d}{dx}f(f^{-1}(x))=\frac{d}{dx}x$$
Apply the chain rule
$$f'(f^{-1}).[f^{-1}]'(x)=1$$
And we're there
$$[f^{-1}]'(x)=\frac{1}{f'(f^{-1}(x))}$$

![[Pasted image 20260412114141.png| 555]]
![[Pasted image 20260412114041.png | 555]]
![[Pasted image 20260412114102.png | 555]]

