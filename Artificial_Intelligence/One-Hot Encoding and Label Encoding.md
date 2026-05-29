Note: Both are Subset of Categorical Encoding
## One Hot Encode 
For the "color" variable, one-hot encoding would create **"color_red", "color_green", and "color_blue" columns, with 1 or 0 in each represent TRUE or FALSE**.
![[Untitled.webp]]
+ $ **Nominal features** *(no inherent order)*, especially with **linear** or **distance-based** models (Logistic Regression, SVM, KNN).  
+ $ Wherever you want the model to treat each category as distict, with no implied ranking.  

## Label Encoding
Instead of creating 3 columns for each color, Label Encoding create 1 column "color" and treat each color as a label. With **0, 1, 2 representing "color_red", "color_green", and "color_blue" respectively**.
![[images 3.png]]
+ $ Use Ordinal Feature *(where order matter)* e.g. `['low', 'medium', 'high']`
+ $ **Tree-based models** (Decision Trees, Random Forests, XGBoost)** often handle integer-encoded categories without introducting surious "distance" effect.  

+ ? **Spurious “distance” effect** in tree base model mean "model might incorrectly associate the distance between a node and the root (or the leaves) with a feature's importance"


| Feature Type     | Label Encode                              | One-Hot Encode                          |
| :--------------- | :---------------------------------------- | :-------------------------------------- |
| **Ordinal**      | ✔ preserves order (“small”<“med”<“large”) | ❌ loses order (unless you manually map) |
| **Nominal**      | ⚠️may introduce spurious order            | ✔ treats each category equitably        |
| **Model Family** | ✔ Decision Trees, RandomForest, XGBoost   | ✔ Linear models, distance-based models  |
| **Cardinality**  | ✔ scales to many categories               | ⚠️ high memory if too many categories   |


