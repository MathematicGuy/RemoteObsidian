# Quantum Computing Foundations

Quantum computing leverages quantum mechanical phenomena to perform complex computational tasks. This note summarizes quantum gates, qubits, and basic quantum algorithms.

## Qubits and Superposition
A classical bit can represent 0 or 1. A qubit can exist in a superposition of both states:
$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$$
where $\alpha, \beta \in \mathbb{C}$ and $|\alpha|^2 + |\beta|^2 = 1$.

## Entanglement
Quantum entanglement allows qubits to share a state, enabling non-local correlations that classical systems cannot replicate.

## Shor's Algorithm
Shor's algorithm solves the prime factorization problem in polynomial time $O((\log N)^3)$, exponentially faster than the best-known classical algorithms.
