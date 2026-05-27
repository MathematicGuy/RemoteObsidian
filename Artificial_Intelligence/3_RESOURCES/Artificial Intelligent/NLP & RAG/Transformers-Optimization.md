# Transformers Optimization Notes

This note covers the core concepts of Transformer model optimization, focus on dynamic model pruning, weight quantization (e.g. INT8 and FP4 formats), and knowledge distillation.

## Quantization
We map floating point weights $W$ to integer representations $q$ using:
$$q = \text{round}\left(\frac{W}{S}\right) + Z$$
where $S$ is the scale factor and $Z$ is the zero-point. This reduces memory footprint by 4x.

## Pruning
Structured pruning removes entire attention heads and feed-forward sub-networks based on activation L2-norms, preserving tensor cores alignment for maximum inference speedups.
