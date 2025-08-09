### Section 1: Vector Database and Distance Loss
SQL – Structure Data (e.g. bảng, json, csv) - MySQL, Oracle, SQLServer, PostgreSQL.
	-> Web/Mobile App, Enterprise Information System. 
NoSQL – Unstructure Data (e.g. dữ liệu chưa được xử lý, video, âm thanh, raw text) - 
+ ? Các phương pháp trên giúp lưu thông tin và truy cập nó qua 1 đường link. e.g. lưu ảnh trong Databse và truy cập thông tin của ảnh đó qua image_link.  
VectorDB – Vector Data: Hoạt động tương tự nhưng nhanh hơn sử dụng Vector. 

**Calculate image similarity by calc distance loss** with L1 or L2 for each pixels between 2 image.  
**L1**
![[Pasted image 20250725112440.png# left | 555]]
**L2**
![[Pasted image 20250725112448.png# left | 555]]

**Inner Product vs Cosine Similarity**
Cosine Similarity: use agnle instead of Inner Product. 

**Dot product**
![[Pasted image 20250725112322.png# left |555]]

**Cosine Similarity:** the bigger the vector angle, the more similarity it has.  
![[Pasted image 20250725112359.png# left | 555]]
`np.linalg`: numpy linear algebra. 

+ ? How do we vectorize text.
```ad-summary
L1, L2 Distance in for similarity search between image pixels.
Cosine Similarity use Angle and Dot Product use Inner Produc to Evaluate similar image from distance. 
```


### Section 3 Project: Check Attendance
**Calcualte Distance Loss with tokenization**
![[Pasted image 20250725112556.png# left | 555]]
Other Vectorize methods than Onehot Vector Encoding:
Dictionary Vectorize, Count Vectorizer, TF-IDF, Word2Vec, Sentence Transformers, BERT. 

Note: FAISS vector database compare vectors with L2 (Euclidean) or Dot Product (Inner Product).  

#### Check Attendance Application
![[Pasted image 20250725112736.png#left | 455]]
The application convert images to vecor then index and calc similarity between Input Image and Image stored inside the Image Vector Database. 
![[Pasted image 20250725130016.png| 400]]
**Method 1 to Convert Image to Vector (pixel value vector)** -> Faster but less accurate.
Each pixel of a Image is a like vector (x, y) each with value from 0 to 255. For 3D image, there're 3 channel for 3 color Red, Blue and Green, to compare each pixels between 2 image, we flatten them, this mean we convert them into 1D vector for easier calculation.   

Note: If the image is gray scale, you would need to convert them into 3D vector then flatten them after. 

**Method 2: Using Deep Learning Model to convert image into Feature Map (multiple matrix instead of vector)** -> Accurate but slightly slower.
This step require you to import InceptionResnetV1 model which train on `vggface2` dataset. You use DL model to convert image into a feature map then use `.unsqueeze` to Flatten it into 1D vector. After that index like normal.  


**Indexing** (the same for both method)
You can use FAISS IndexFlatL2/IndexIP (L2 / Inner Product) for Image vector search or use Deep Learning Model to search using Feature Map. 
	Indexing would return n images, so set a limit k if you just need 5 best result.

### Section 4 Project: Cocktail Suggestion
[**pgvector**](https://github.com/pgvector/pgvector)
![[Pasted image 20250725112913.png# left|555]]
**Supabase** allow you to use and host Postgres database without installing it. 
**pgdb Operator for indexing:**
`<->` L2 distance
`<#>` (negative) inner product
`<=>` cosine distance
`<+>` L1 distance
`<~>` Hamming distance (binary vectors)
`<%>` Jaccard distance (binary vectors)

**IVFFlat** (Indexing on Cluster data)
**HNSW** (Indexing on Graph data)
![[Pasted image 20250725113017.png# left | 500]]

**psycopg2: PostgreSQL Adapter for Python**
![[Pasted image 20250725113111.png# left | 555]]
>Import and use through Supabase 

**Project Objective**
![[Pasted image 20250725113209.png# left|555]]
**Dataset:** https://www.kaggle.com/datasets/aadyasingh55/cocktails/data
	This dataset contains a collection of drink recipes, providing essential details for each recipe.
**Features:**  
	**id:** Unique identifier for each drink.  
	**name:** Name of the drink.  
	**alcoholic:** Indicates whether the drink is alcoholic or non-alcoholic.  
	**category:** Type of drink (e.g., Cocktail, Ordinary Drink).  
	**glassType:** Recommended glass type for serving.  
	**instructions:** Preparation instructions for the drink.  
	**drinkThumbnail:** Image thumbnail of the drink.  
	**ingredients:** List of ingredients used in the recipe.  
	**ingredientMeasures:** Measurements corresponding to each ingredient.

#### Data Processing


#### Search suitable cocktail



+ ? Logistic -> Optimal Transfer
