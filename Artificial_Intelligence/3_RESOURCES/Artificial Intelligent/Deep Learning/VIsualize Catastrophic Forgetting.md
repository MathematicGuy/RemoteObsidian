**Representational Analysis (t-SNE, PCA)**: Techniques like t-distributed stochastic neighbor embedding (t-SNE) are used to visualize the high-dimensional *feature representations* (embeddings) learned *by the network's internal layers* in a 2D or 3D space.
+ ? Check how classes distribution changed before & after forgetting. 
	
- **Before Forgetting**: *Clusters of data points* corresponding to different classes from the first *task are clearly separated
	
- **After Forgetting**: After training on a new task, the *clusters for the old classes might overlap significantly with the new ones* **or** *become entirely misaligned*, illustrating "inter-phase confusion". This shows how the decision boundaries have shifted dramatically.

**Heatmaps of Important Weights**: Methods like EWC identify which weights are "critical" for previous tasks using metrics like the Fisher Information Matrix.
- ? **Visualization**: Heatmaps can show **which layers or specific parameters change the most when new tasks are learned.**
	Studies have found that deeper layers are often disproportionately affected by forgetting.
