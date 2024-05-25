
**Youtube Turtorial:** https://youtu.be/Wz3nbQPYwss 

## Step I: Set Up

#### 1) Have an Image (jpg, png, etc..)

#### 2) Set Wrap mode to REPEAT
	Advance > Wrap Mode > Select REAPEAT

#### 3) Create 3D Background 
	Create Empty > 3D > Quad
Set **Quad** size to **fit Camera** (16:9 Scale) and Change its **name to "ScrollingBackground"** 


## Step II:  Background

#### 3D View > Move Quad behind the Main Object  
#### Delete Quad "Mesh Collider" 

#### Create **Material** in Project
	Material > Shader > Select Unlit > Unit/Texture 
	Texture > Add **Setup Image**  

## Step III: Material

#### Create ScrollingBacgrooundScript 
	Add Script to Quad > Set Speed to 0.2 
	Drag Mesh Renderer to Bg Renderer   
	**!! Finish !!**
```cs
using UnityEngine;

public class ScrollingBackGroundScript : MonoBehaviour
{
    public float speed;

    [SerializeField]
    private Renderer bgRenderer;

    private void Update()
    {
        // Vector2(transform_speed, initial speed)
		bgRenderer.material.mainTextureOffset += new                                 UnityEngine.Vector2(speed * Time.deltaTime, 0);         
    }
}
```
