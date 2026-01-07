**Joint Training:** baseline model **trained** on data from **all tasks simultanously.** 

**Learning (Plasticity):** Gravity pulling the ball down into a valley (low error for the current task).

**Forgetting:** When the ball moves to a new valley for Task B, it is no longer in the valley for Task A.

**Forward Transfer (FWT):** The influence of **previously learned tasks on the performance of future tasks** (positive FWT means knowing Task A helps learn Task B faster).

**Backward Transfer (BWT):** The **influence of learning a new task on the performance of previously learned tasks.** Negative BWT indicates catastrophic forgetting; positive BWT indicates that learning a new task actually improved performance on an old one.

**Regularization (EWC):** **Attaching a spring to the ball anchored at the bottom of Task A's valley**. The spring is stiff **(hard to pull) for important parameters and loose for unimportant ones.** This allows the ball to move toward Task B's valley but prevents it from leaving Task A's valley entirely.


**Herding:** a deterministic strategy for selecting **which samples to store in memory (for replay)** based on finding **samples that best the approx class mean in feature space.** 

**Methodological Approach** (Taxonomy - phân loại)
+ **Replay-based Approach:** Focuses on approximating and recovering old data distributions to train alongside new data.
+ **Optimization-based Approach:** Explicitly manipulates the optimization program (e.g., gradients).
+ **Architecture-based Approach:** Uses specific network structures to reduce interference. 
	+ Model Decomposition: Seperates the model into task-sharing and task-specific components. 
	+ Modular Netowork: Parralel sub-network for different tasks.
	+ Parameter Allocation: dedicate specific subspaces of params to specific tasks. (e.g., using masks to *freeze weights for old tasks*)

