
### Summary Table of Probability Symbols

| Symbol               | Meaning                                  |
| -------------------- | ---------------------------------------- |
| $\cup$               | Union (either $A$ or $B$ occurs)         |
| $\cap$               | Intersection (both $A$ and $B$ occur)    |
| $A^c$                | Complement (event $A$ does not occur)    |
| $\emptyset$          | Empty set (impossible event)             |
| $\setminus$          | Set difference ($A$ but not $B$)         |
| $\subset, \subseteq$ | Subset relationship                      |
| $P(A)$               | Probability of event $A$                 |
| $P(A \mid B)$        | Conditional probability of $A$ given $B$ |
| $\Omega$             | Universal set or sample space            |


### 1. **Union ($\cup$)**
   - **Meaning**: The union of two events $A$ and $B$, denoted $A \cup B$, represents the event that **either event $A$ or event $B$, or both, occur**.
   - **Example**: If $A$ represents the event "rolling an even number" and $B$ represents the event "rolling a number greater than 4", then $A \cup B$ represents rolling an even number or a number greater than 4.

### 2. **Intersection ($\cap$)**
   - **Meaning**: The intersection of two events $A$ and $B$, denoted $A \cap B$, represents the event that **both events $A$ and $B$ occur simultaneously**.
   - **Example**: If $A$ represents rolling an even number and $B$ represents rolling a number greater than 4, then $A \cap B$ represents rolling the number 6, which is both even and greater than 4.

### 3. **Complement ($A^c$ or $\overline{A}$)**
   - **Meaning**: The complement of an event $A$, denoted $A^c$ or sometimes $\overline{A}$, represents the event that **$A$ does not occur**.
   - **Example**: If $A$ represents rolling a number greater than 3 on a die, then $A^c$ represents rolling a number less than or equal to 3.

### 4. **Empty Set ($\emptyset$)**
   - **Meaning**: Represents the **empty set**, or an event that **cannot occur** (i.e., it has zero probability).
   - **Example**: If $A$ and $B$ are two mutually exclusive events, then $A \cap B = \emptyset$.

### 5. **Set Difference ($A \setminus B$)**
   - **Meaning**: The set difference $A \setminus B$ represents the elements in event $A$ that are **not in event $B$**.
   - **Example**: If $A$ represents rolling an even number and $B$ represents rolling a number greater than 4, then $A \setminus B$ represents rolling 2.

### 6. **Subset ($\subset$ or $\subseteq$)**
   - **Meaning**: $A \subset B$ means that **event $A$ is a subset of event $B$**; that is, every outcome in $A$ is also in $B$.
   - **Example**: If $A$ is rolling a 2 and $B$ is rolling an even number, then $A \subset B$.

### 7. **Probability ($P(A)$)**
   - **Meaning**: $P(A)$ represents the **probability** of event $A$ occurring.
   - **Example**: If rolling a fair die, $P(\text{rolling a 4}) = \frac{1}{6}$.

### 8. **Conditional Probability ($P(A \mid B)$)**
   - **Meaning**: The **conditional probability** of event $A$ given that event $B$ has occurred, denoted $P(A \mid B)$, represents the **probability of $A$ occurring assuming $B$ has occurred**.
   - **Example**: If $A$ is rolling an even number and $B$ is rolling a number greater than 3, $P(A \mid B)$ is the probability of rolling an even number given that the roll is greater than 3.

### 9. **Intersection Probability ($P(A \cap B)$)**
   - **Meaning**: Represents the probability that **both events $A$ and $B$ occur**.
   - **Example**: If $A$ and $B$ are independent events, then $P(A \cap B) = P(A) \times P(B)$.

### 10. **Union Probability ($P(A \cup B)$)**
   - **Meaning**: Represents the probability that **either event $A$, event $B$, or both occur**.
   - **Formula**: 

   $$
   P(A \cup B) = P(A) + P(B) - P(A \cap B)
   $$

   - **Example**: If $A$ and $B$ are rolling an even number and rolling greater than 4 respectively, then $P(A \cup B)$ represents the probability of rolling either an even number or a number greater than 4.

### 11. **Mutually Exclusive Events**
   - **Symbolically**: For mutually exclusive events $A$ and $B$, $A \cap B = \emptyset$.
   - **Meaning**: Two events $A$ and $B$ are **mutually exclusive** if they **cannot occur at the same time**.
   - **Example**: Rolling a 3 and rolling a 4 on a single die are mutually exclusive events.

### 12. **Universal Set ($\Omega$)**
   - **Meaning**: Represents the **sample space** or **universal set** of all possible outcomes.
   - **Example**: In rolling a die, $\Omega = \{1, 2, 3, 4, 5, 6\}$.

### 13. **Addition Rule of Probability**
   - For two events $A$ and $B$:

   $$
   P(A \cup B) = P(A) + P(B) - P(A \cap B)
   $$

   This rule is used to find the probability that **either $A$ or $B$, or both, occur**.

