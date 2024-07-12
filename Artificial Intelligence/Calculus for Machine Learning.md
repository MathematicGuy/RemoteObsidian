# Derivatives and Optimization
## Machine Learning Motivation
```ad-faq
Why Derivitive and Calculus -> Optimize function. Find Maximum and Minimum value
-> Help to find the model that fits my data in the best possible way (calc loss func and minimizing it)
```


Given a classification problem, we got the graph below. Say we want to classified a region for sad and happy.
![[Pasted image 20240710074612.png]]
![[Pasted image 20240710074806.png]]

We would like to train the Model to tweak the classifier line to this position. 
![[Pasted image 20240710074722.png]]
+ ? So how the Model do this...

## Motivation to Derivatives - Part 1

![[Pasted image 20240710075538.png]]
> No, you calculate the speed by the distance t travel by the time: v = S / t
> Or calculate the distance it travel after a period of times.
> ![[Pasted image 20240710075744.png]]

> We can calculate the the average speed between a time interval and distance by dividing the changes in distances to times.
![[Pasted image 20240710080116.png]]


+ ? But, can we estimate the velocity of the car at time t = 12.5. Let's try using the slope 
	![[Pasted image 20240710080426.png]]
	![[Pasted image 20240710081706.png]]
	So the speed is more accurate this time. When we make the interva of time (t) and 
	distance (x) closer to eachother. 
	![[Pasted image 20240710082554.png]]
	And if we put the interval to be super close to each others. You get the limit which is dx over dt and that is precisely the tangent line to the curve at t equals 12.5
	![[Pasted image 20240710082148.png]]
	+ $ **Instantaneous rate of change is a measure of how fast the relation between two variables is changing at any point**. In other words, **imagine you move a tiny distance, dx in a tiny interval of time dt**. This is the instantaneous rate of change. -> It's also called **Derivative.**

> Like anything else, v = 0, if no distance changes in time.
![[Pasted image 20240710084453.png]]

## Derivatives and their notation
2 ways to express derivative: **Leibniz's notation** and **Lagrange's notation.**

![[Pasted image 20240710085121.png]]]]
![[Pasted image 20240710085315.png]]

## Some Common Derivative
### Lines
![[Pasted image 20240710085528.png]]

+ ? Slope is the changes of rise over run. Using Pythagorean, we conclude that $\frac{\nabla y}{\nabla x} = a$ 
![[Pasted image 20240710093127.png]]
So when 2 points are so close to each other it like they're in 1 position. We can say that f(x)' = a. Let's proven it more clearly
![[Pasted image 20240710085720.png]]
we have f(x) = y(x) as the line function
The 1st point have x as x and y as ax + b (typical line's function)
The 2nd point have  x as (x + $\nabla x$) so y must be a(x + $\nabla x$) + b
+ $ Now, apply the derivative for those 2 points. we achieve:
![[Pasted image 20240710090540.png]]
As we cancel out, what is left is:  a
![[Pasted image 20240710090615.png]]

### Quadratics
$\nabla f$ = y2 - y1. and if y1 = x^2 <->  y2 = $(x + \nabla x)^2$ with $\nabla x \in R$
![[Pasted image 20240710171435.png]]
Repeat the same step as the interval smaller and smaller. We finally got the result close to 2
![[Pasted image 20240710171142.png]]
![[Pasted image 20240710171803.png]]
> **As 2 points move closer**, $\nabla x \to 0$ (delta_x move closer to 0. the same for delta_y) There for the **Derivative of Quadratics function is: 2x**
![[Pasted image 20240710172234.png]]

### Higher degree polynomials 
#### Derivatvative of Cubic Functions
![[Pasted image 20240710172608.png]]
>Like before, we calculate the slope. The 1st one is 3.25 as $\nabla x$ is 1. Decrease the interval between 2 points and repeat the same step we got
![[Pasted image 20240710172917.png]]
So the result is as close as $3*0.5^{2} \approx 0.75$. This seem true since the derivative is actually  $3x^2$  
+ ? Let simplified the Slope and see what we got: Like before $\nabla x \to 0$ and we really got 
 the **Derivative of a Cubic is** $$3x^2$$ 
![[Pasted image 20240710173035.png]]

### Other power functions
> Like before, we calc the slope of a value. Then move the interval closer and closer.
![[Pasted image 20240710173642.png]]
![[Pasted image 20240710174409.png]]
 Simplified the Slope we got
![[Pasted image 20240710174828.png]]
 When you calc the Derivative of others power function, you can see there a pattern of (Power - 1):  $$\frac{d}{dx}f(x) = nx^{n-1}$$ 
![[Pasted image 20240710175119.png]]


## The Inverse Function and Its Derivative

If a function does a thing, the inverse function inverse that thing:
+ ? F(x) turn 1 to 5. So the inverse of F(x) will turn 5 into 1
### Inverse function
![[Pasted image 20240712084624.png]]

The 1st function have y = f(X) thus g(y) = $\sqrt{f(x)}$ 
![[Pasted image 20240712084813.png]]
+ secant: đường cát tuyến (đường cắt)


> Derivative = change in horizontal / change in vertical. Therefor
> 1st Slope: $\frac{\nabla f}{ \nabla x}$  & 2st Slope: $\frac{\nabla y}{\nabla g}$. 
+ ? Because g(y) and f(x) is just inverse of points. Their value doesn't changed, this mean $\nabla f$ = $\nabla y$  and $\nabla g$ = $\nabla x$. 

+ $ Let call the 1st Slope as f(x)' and 2nd slope as g(y)'. Since  g(y)' = f(x)' in reverse y-axis  $=> g(y) = \frac{1}{f(x)'}$    (just imagin 2 = 1/2 -> 2 = 1/(1/2))
![[Pasted image 20240712085418.png]]

**Examples**
![[Pasted image 20240712090826.png]]
![[Pasted image 20240712091033.png]]

## Derivative of Trigonometic  
note: revison some trigonometry
 ![[Pasted image 20240712093458.png]]

![[Pasted image 20240712093939.png]]

+ ? $\sin(x + \nabla x)$ is a point with $\nabla x$ as a natural number. We see that $\sin (x + \nabla x) > \sin x$
+ ? $\cos(x + \nabla x)$ also a point like sin. But $\cos(x + \nabla x) < \cos(x)$ 
+ [[Explain -delta(cos x)]] :  $-\nabla(\cos x)$  
	+ $ The change in the x-coordinate (cosine value) as we move from x to $x + \Delta$ is given by $\Delta(\cos x) = \cos(x + \Delta x) - \cos(x)$
		
	+ $ When $Δ(cos⁡x)$ is negative, it means the x-coordinate (cosine value) has decreased.
		
	- $ To visually and mathematically represent this decrease, we use the term $-\Delta(\cos x)$.
![[Pasted image 20240712094405.png]]

+ $ As the **trigangle shrink smaller and smaller (cause derivative) the hypotenuse align with the arc of the circle** (cung của hình tròn), thus making h = $\Delta x$
![[Pasted image 20240712094520.png]]
Replacing the 2 values. We achieve:
![[Pasted image 20240712094531.png]]

$\frac{\Delta(\sin x)}{\Delta x} = \cos x$  and  $-\frac{\Delta(\cos x)}{\Delta x} = \sin(x)$
 
 This actually comfirms the intuition we built before:
![[Pasted image 20240712103604.png]]


