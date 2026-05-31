### Normalization or Standardizationda
- **Normalization**: Scaling features to a range, typically `[0, 1]`.
    - Formula: $$x_{norm}=\frac{x - \min(x)}{\max(x) - \min(x)}$$
- **Standardization**: Scaling features to have a mean of 0 and a standard deviation of 1.
    - Formula: $$x_{standard} = \frac{x - \mu}{\sigma}$$
+ $ By scaling, we ensure that the features are on the same scale, which results in more balanced gradient updates and leads to faster and more stable convergence.

